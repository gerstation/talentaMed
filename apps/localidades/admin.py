
# coding: utf-8
from django.contrib import admin
from .models import Municipio, Region
# Register your models here.

class MunicipioAdmin(admin.ModelAdmin):
    fieldsets = [[
        ('Básico'), {
        'fields': (
            'codigo', 'texto', 'activo'
        )
    }]]

class RegionAdmin(admin.ModelAdmin):
    filter_horizontal = ('municipio',)
    fieldsets = [
        [
            ('Básico'), {
            'fields': (
                'codigo', 'texto'
            )
        }],
        [
            ('Configuración municipal'), {
                'fields': ('municipio',)
        }],
    ]

admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Region, RegionAdmin)