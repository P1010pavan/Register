from django.urls import path
from . import  views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index1,name='register'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)