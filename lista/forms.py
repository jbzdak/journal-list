# coding=utf-8
__author__ = 'jb'

from django import forms

order_by = (
    (0, '----'),
    (1, "Name"),
    (2, "ISSN"),
    (3, "pts")
)

from models import categories


class SearchForm(forms.Form):
    name = forms.CharField(label="Nazwa czasopisma", required=False)
    pts = forms.IntegerField(label=u"Więcej niż tyle punktów", required=False)
    issn = forms.CharField(label = "ISSS", required=False)
    order_by = forms.ChoiceField(choices=order_by, initial = 0, required=False)
    cathegory = forms.ChoiceField(choices=((0, "-----"),) + categories, initial = 0, required=False)



