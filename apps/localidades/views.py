from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.urls import reverse
from django.utils.functional import lazy
reverse_lazy = lambda *args, **kwargs: lazy(reverse, str)(*args, **kwargs)
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin
from .models import *
from .forms import (
    MunicipioForm,
    RegionForm,
)

http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

class Home(ListView):
    model = Municipio
    context_object_name = 'localidades'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        return context


class HomeMunicipioView(ListView):
    model = Municipio
    context_object_name = 'municipios'
    template_name = 'municipios.html'

    def get_queryset(self):
        return Municipio.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(HomeMunicipioView, self).get_context_data(**kwargs)
        municipios = Municipio.objects.all()
        context['municipios'] = municipios
        return context


class HomeRegionView(ListView):
    model = Region
    context_object_name = 'regiones'
    template_name = 'regiones.html'

    def get_queryset(self):
        return Region.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(HomeRegionView, self).get_context_data(**kwargs)
        regiones = Region.objects.all()
        context['regiones'] = regiones
        return context   


# VISTAS DE FORMULARIOS

class MunicipioFormView(CreateView):
    form_class = MunicipioForm
    template_name = 'form.html'

    def __init__(self, *args, **kwargs):
        super(MunicipioFormView, self).__init__(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        self.response = True
        return super(MunicipioFormView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        data = super(MunicipioFormView, self).get_context_data(**kwargs)
        data['form'] = self.get_form()
        return data
    
    def get_form_kwargs(self):
        kwargs = super(MunicipioFormView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_success_url(self):
        return reverse('municipios')


class RegionFormView(CreateView):
    form_class = RegionForm
    template_name = 'form.html'

    def __init__(self, *args, **kwargs):
        super(RegionFormView, self).__init__(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        self.response = True
        return super(RegionFormView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        data = super(RegionFormView, self).get_context_data(**kwargs)
        data['form'] = self.get_form()
        return data
    
    def get_form_kwargs(self):
        kwargs = super(RegionFormView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_success_url(self):
        return reverse('regiones')



class MunicipioDeleteFormView(DeleteView):
    model = Municipio
    template_name = 'modules/delete.html'
    success_url = reverse_lazy('municipios')


class RegionDeleteFormView(DeleteView):
    model = Region
    template_name = 'modules/delete.html'
    success_url = reverse_lazy('regiones')


class MunicipioUpdateFormView(UpdateView):
    model = Municipio
    success_url = reverse_lazy('municipios')
    fields = ['codigo', 'texto', 'activo']
    template_name = 'form.html'

class RegionUpdateFormView(UpdateView):
    model = Region
    success_url = reverse_lazy('regiones')
    fields = ['codigo', 'texto', 'municipio']
    template_name = 'form.html'
    