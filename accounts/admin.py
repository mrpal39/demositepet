from django.contrib import admin

from .models import  OwnerProfile


class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        
    )

admin.site.register(OwnerProfile, OwnerProfileAdmin)
