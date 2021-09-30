from django.db import models

import datetime

# Create your models here.


TURNO = [
		("MATUTINO", "Matutino"),
		("VESPERTINO", "Vespertino"),
		("NOCTURNO", "Nocturno"),
		("MOVIL", "Movil"),
	]

SEXO = [
		("HOMBRE", "Hombre"),
		("MUJER", "Mujer"),
	]

PROFESION = [
    ("SI", "Si"),
    ("NO", "No"),
]

DESPENALIZACION = [
    ("A FAVOR", "A Favor"),
    ("EN CONTRA", "En Contra"),
]



class ConsultaSituacionalModel(models.Model):
    class Meta:
        db_table = 'encuestaSituacionalTable'
        app_label = 'encuestaSituacional_db'

    categoria = models.CharField(max_length=150, null=False, blank=False)
    adscripcion = models.CharField(max_length=150, null=False, blank=False)
    turno = models.CharField(max_length=15, null=False, blank=False, choices=TURNO)
    sexo = models.CharField(max_length=10, null=False, blank=False, choices=SEXO)
    antiguedad = models.CharField(max_length=30, null=False, blank=False)
    primera = models.CharField(max_length=250, null=False, blank=False)
    segunda = models.CharField(max_length=10, null=False, blank=False, choices=PROFESION)
    tercera = models.CharField(max_length=250, null=False, blank=False)
    cuarta = models.CharField(max_length=100, null=False, blank=False, choices=DESPENALIZACION)
    quinta = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(deafult=datetime.datetime.now())
