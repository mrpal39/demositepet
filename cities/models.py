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
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50,null=True,blank=True)
    objects=StateManager()
    class Meta:
        ordering = ["name"]


    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=500)
    state = models.ForeignKey('State', on_delete=models.CASCADE,null=True)
    code= models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name

    def get_state(self):
        return self.state.name

class City(models.Model):
    name = models.CharField(max_length=500)
    code= models.CharField(max_length=500)
    district = models.ForeignKey('District', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    def get_state(self):
        return self.district.state.name


    def get_district(self):
        return self.district.name


    def state(self):
        return self.district.state.id

