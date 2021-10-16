from django.contrib import admin

# Register your models here.

from .models import Bread, Category, Pet


admin.site.register(Pet)

admin.site.register(Bread)

admin.site.register(Category)
