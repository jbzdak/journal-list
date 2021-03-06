# coding=utf-8
# Create your views here.
from itertools import chain
from django.db.models import Q
from django.template.response import TemplateResponse

import forms
import models

def search_fun(name = None, pts = None, issn = None, cathegory = None, order_by = None, phrase=False):
    name_replacements = (
        (u"ż", "z"),
        (u"ó", "o"),
        (u"ł", "l"),
        (u"ć", "c"),
        (u"ę", "e"),
        (u"ś", "s"),
        (u"ą", "a"),
        (u"ź", "z"),
        (u"ń", "n")
    )

    q_objects = []

    qs = models.Journal.objects.filter()

    if pts:
        q_objects.append(Q(pts__gte = pts))
    if issn:
        q_objects.append(Q(issn__icontains = issn))
    if cathegory:
        cathegory = int(cathegory)
        if cathegory != 0:
            q_objects.append(Q(cathegory = cathegory))

    if name:
        name_non_pl = name
        for pl, en in name_replacements:
            name_non_pl = name_non_pl.replace(pl, en)
            name_non_pl = name_non_pl.replace(pl.upper(), en.upper())

        qs = models.Journal.objects.filter(*q_objects)

        if phrase:
            if name_non_pl != name:
                qs = qs.filter(Q(name__icontains =  name) | Q(name__icontains =  name_non_pl))
            else:
                qs = qs.filter(name__icontains =  name)
        else:
            for pl, non_pl in zip(name_non_pl.split(), name.split()):
                if pl != non_pl:
                    qs = qs.filter(Q(name__icontains =  pl) | Q(name__icontains =  non_pl))
                else:
                    qs = qs.filter(name__icontains =  pl)

    else:
        qs = models.Journal.objects.filter(*q_objects)

    if order_by:
        order_by = int(order_by)

        if order_by == 2:
            qs = qs.order_by("issn")
        elif order_by == 3:
            qs = qs.order_by("-pts", "name", "issn")
        else:
            qs = qs.order_by("name")

  #  print(repr(str(qs.query)))
    return qs

def search(request):
    form = forms.SearchForm()
    results = None
    if request.method == "POST":
        form = forms.SearchForm(data = request.POST)
        if form.is_valid():
            results = search_fun(**form.cleaned_data)
    return TemplateResponse(request, "search.html", {
        "form" : form,
        "results" : results
    })

