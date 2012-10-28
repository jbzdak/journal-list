from django.db import models

# Create your models here.

categories = (
    (1, "Posiada Impact Factor"),
    (2, "Nie posiada Impact Factor"),
    (3, "W indeksie ERIH")
)

class Journal(models.Model):

    issn = models.CharField(max_length=9, primary_key=True)
    name = models.TextField(verbose_name="Nazwa czasopisma", db_index=True)
    pts = models.PositiveSmallIntegerField(verbose_name="Punkty za czasopismo", db_index=True)
    cathegory = models.PositiveSmallIntegerField(verbose_name="Kategoria", db_index=True, choices=categories)