from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import *
from .forms import (
    MunicipioForm,
    RegionForm,
)

http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

# class Home(ListView):
#     model = Empleado
#     context_object_name = 'localidades'
#     template_name = 'home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super(Home, self).get_context_data(**kwargs)
#         return context


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


class MunicipioDetailView(DetailView):
    model = Municipio 
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    template_name = 'modules/detalle_municipio.html'

    def get_queryset(self):
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.all()
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.queryset.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if slug is None:
            raise AttributeError("Generic detail view %s must be called with "
                                "either an object pk or a slug."
                                % self.__class__.__name__)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise http.Http404("No %(verbose_name)s found matching the query" %
                        {'verbose_name': queryset.model._meta.verbose_name})
        return obj


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


class RegionDetailView(DetailView):
    model  = Region
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    template_name = 'modules/detalle_region.html'

    def get_queryset(self):
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.all()
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.queryset.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        if slug is None:
            raise AttributeError("Generic detail view %s must be called with "
                                "either an object pk or a slug."
                                % self.__class__.__name__)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise http.Http404("No %(verbose_name)s found matching the query" %
                        {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class MunicipioFormView(FormMixin, HomeMunicipioView):
    form_class = MunicipioForm

    def __init__(self, *args, **kwargs):
        super(MunicipioFormView, self).__init__(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

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


class RegionFormView(FormMixin, HomeRegionView):
    form_class = RegionForm

    def __init__(self, *args, **kwargs):
        super(RegionFormView, self).__init__(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

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
