# coding: utf-8
import string
from django.db import models
from django.core.exceptions import ValidationError


def _codigo_simple_validator(value):
    if not value:
        return
    checks = ((s in value) for s in string.whitespace)
    if any(checks):
        raise ValidationError(
            (u"El código no debe contener espacios ni tabuladores."),
        )


class Municipio(models.Model):
    codigo = models.CharField(
        (u"Código"),
        max_length=10,
        unique=True,
        db_index=True,
        validators=[_codigo_simple_validator],
    )
    texto = models.CharField(
        (u"Descripción"), 
        max_length=30)
    activo = models.BooleanField(
        (u'Activo'), default=True)
    
    class Meta:
        verbose_name = (u"Municipio")
        verbose_name_plural = (u"Municipios")
    
    def __unicode_(self):
        return self.texto



class Region(models.Model):
    codigo = models.CharField(
        (u"Código"),
        max_length=10,
        unique=True,
        db_index=True,
        validators=[_codigo_simple_validator],
    )
    texto = models.CharField(
        (u"Descripción"), 
        max_length=30)
    municipio = models.ManyToManyField(
        Municipio, blank=True,
        verbose_name=(u"Municipios"))

    class Meta:
        verbose_name = (u"Región")
        verbose_name_plural = (u"Regiones")
    
    def __unicode_(self):
        return self.texto