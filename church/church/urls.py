from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('rcf.urls')),  # Including rcf app's urls
    
    # Sunday School app URLs
    path('sunday/', include('sunday.urls')),  # Including sunday_school app's urls
     path('sermon/', include('sermon.urls')),
     path('contact/', include('contact.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
