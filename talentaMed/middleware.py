
from django.core.exceptions import ObjectDoesNotExist
from apps.localidades.models import *

class TalentaMed(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        data = self._localidades(request)
        for key, value in data.items():
            if value is not None:
                setattr(request, key, value)
            elif hasattr(request, key):
                delattr(request, key)
    
    def _localidades(self, request):

        try:
            municipios = Municipio.objects.all()
        except ObjectDoesNotExist:
            municipios = None
        try:
            regiones = Region.objects.all()
        except ObjectDoesNotExist:
            regiones = None
        print("#"*100)
        data = {
            'municipios': municipios,
            'regiones': regiones
        }
        return data