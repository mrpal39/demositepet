from django.contrib.admin import AdminSite
class EventAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"

event_admin_site = EventAdminSite(name='event_admin')

from accounts.models import OwnerProfile
# 

# class OwnerProfileAdmin(admin.ModelAdmin):
#     list_display = (
#         "username",
#         "first_name",
#         "last_name",
#         "date_joined",
#         "last_login",
#         "is_information_confirmed",
#     )
#     list_filter = ("date_joined", "last_login", "is_information_confirmed")


# admin.site.register(OwnerProfile, OwnerProfileAdmin)


event_admin_site.register(OwnerProfile)
# event_admin_site.register(Event)
# event_admin_site.register(EventHero)
# event_admin_site.register(EventVillain)