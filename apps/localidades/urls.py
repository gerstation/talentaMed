from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^municipios/$', HomeMunicipioView.as_view(), name="municipios"),
    url(r'^add-municipios/$', MunicipioFormView.as_view(), name="add_municipio"),
    url(r'^delete-municipios/(?P<pk>\d+)$', MunicipioDeleteFormView.as_view(), name="delete_municipio"),
    url(r'^update-municipios/(?P<pk>\d+)$', MunicipioUpdateFormView.as_view(), name="update_municipio"),
    url(r'^regiones/$', HomeRegionView.as_view(), name="regiones"),
    url(r'^add-regiones/$', RegionFormView.as_view(), name="add_region"),
    url(r'^delete-regiones/(?P<pk>\d+)$', RegionDeleteFormView.as_view(), name="delete_region"),
    url(r'^update-municipios/(?P<pk>\d+)$', RegionUpdateFormView.as_view(), name="update_region"),
]