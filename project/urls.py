from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]

debug = settings.DEBUG
media_url = settings.MEDIA_URL
media_root = settings.MEDIA_ROOT
static_url = settings.STATIC_URL
static_root = settings.STATIC_ROOT

if debug:
    urlpatterns += static(media_url, document_root=media_root)
    urlpatterns += static(static_url, document_root=static_root)