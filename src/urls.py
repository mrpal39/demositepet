
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from django.urls.conf import include
from common.views import home_page, api,index
from events.admin import event_admin_site
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('entity-admin/', admin.site.urls),
    path('event-admin/', event_admin_site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home_page, name='homepage'),
    path('base/', index, name='index'),
    path('k/', include('kennels.urls'), name='homepage_kennels'),
    path('pet/', include('pet.urls'), name='homepage'),
    path("api/", api, name='apiView'),
    re_path(r'^filer/', include('filer.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('dd/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'accounts.views.error_404_view'
