from django.db import models

# from cities.querysets import CityQuerySet
from . import utils


class State(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=2,null=True,blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
