
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from django.urls.conf import include
from pet.views import home_page,apiView
from events.admin import event_admin_site


urlpatterns = [
    path('entity-admin/', admin.site.urls),
    path('event-admin/', event_admin_site.urls),
    path('accounts/',include('accounts.urls')),
    path('',home_page,name='homepage'),
    path('pet/',include('pet.urls'),name='homepage'),
    path("api/",apiView,name='apiView')


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns +=[



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'accounts.views.error_404_view'
