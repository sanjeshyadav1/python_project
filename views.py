from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myApp1.views import *

urlpatterns = [
path('Phonebook/',PhoneBook),
  

    path('savecon/',savecon, name='savecon'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)