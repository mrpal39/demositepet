
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from django.urls.conf import include
from common.views import *
from events.admin import event_admin_site


urlpatterns = [

    path('admin/', admin.site.urls),
    # path('event-admin/', event_admin_site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home_page, name='homepage'),
    path('wish/', wishList, name='wishlist'),
    path('search/', searchbar, name='searchbar'),
   #  path('base/', index, name='index'),
    path('k/', include('kennels.urls'), name='homepage_kennels'),
    path('pet/', include('pet.urls'), name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
]

urlpatterns += [
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.api/*',
                        TemplateView.as_view(template_name='register.html'))]

