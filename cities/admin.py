from django.contrib import admin
from .models import  District, State,City


admin.site.register(State)
admin.site.register(District)
admin.site.register(City)