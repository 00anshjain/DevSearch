from django.contrib import admin
from django.urls import path, include
from django.conf import settings   # to get access to settings.py file to get access to MEDIA_ROOT and MEDIA_URL
from django.conf.urls.static import static  #static will help us create url for static files

urlpatterns = [
    path('admin/', admin.site.urls),
    #This admin panel cannot be accessed until we have our database ready.
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
