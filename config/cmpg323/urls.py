# config/urls.py
from django.contrib import admin
from django.urls import path, include # Import this function
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main app
    path('', include('cmpg323.urls')),
    #Authenticate
    path('users/', include('users.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)