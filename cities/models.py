from django.db import models

# from cities.querysets import CityQuerySet
from . import utils
from django.db.models import Q

class StateManager(models.Manager):
    
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query))
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
    
class State(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=2,null=True,blank=True)
    objects=StateManager()
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

