from django.contrib import admin

from kennels.models import Breed, Contact, Kennel

# Register your models here.
admin.site.register(Breed)
admin.site.register(Kennel)
admin.site.register(Contact)
