from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('apps.localidades.urls'), name='localidades')
]
