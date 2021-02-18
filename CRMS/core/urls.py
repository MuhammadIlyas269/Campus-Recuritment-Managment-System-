from django.urls import path
from .views import index
from django.conf import settings 
from django.conf.urls.static import static 

#create urls here 

urlpatterns = [
    path('', index),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)