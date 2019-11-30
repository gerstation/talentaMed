# coding: utf-8
import json
import re
from django import forms
from django.utils.translation import get_language
from .models import Municipio, Region


class MunicipioForm(forms.ModelForm):

    class Meta:
        model = Municipio
        fields = [
            'codigo',
            'texto',
            'activo',
        ]
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MunicipioForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control"
                })

    def clean(self):
        super(MunicipioForm, self).clean()
        return self.cleaned_data


class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = [
            'codigo',
            'texto',
            'municipio'
        ]
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control"
                })

    def clean(self):
        super(RegionForm, self).clean()
        return self.cleaned_data
