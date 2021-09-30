from django.db import models
import datetime

# Create your models here.


class EncuestaModel(models.Model):
	class Meta:
		db_table = 'encuesta'
		app_label = 'encuesta_db'

	CATEGORIA = [
		("MEDICO", "Médico"),
		("ENFERMERA(O)", "Enfermera(o)"),
	]

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

	PRIMERA = [
		("SI", "Si"),
		("CUANTOS", "Cuantos"),
		("NO", "No"),
	]

	SEGUNDA = [
		("SI", "Si"),
		("NO", "No"),
	]


	categoria = models.CharField(max_length=150, null=False, blank=False, choices=CATEGORIA)
	adscripcion = models.CharField(max_length=150, null=False, blank=False)
	turno = models.CharField(max_length=15, null=False, blank=False, choices=TURNO)
	sexo = models.CharField(max_length=10, null=False, blank=False, choices=SEXO)
	antiguedad = models.CharField(max_length=30, null=False, blank=False)
	primera = models.CharField(max_length=10, null=False, blank=False, choices=PRIMERA, default="SI")
	segunda = models.CharField(max_length=4, null=False, blank=False, choices=SEGUNDA, default="SI")
	tercera = models.IntegerField(default=1, null=False, blank=False)
	cuarta = models.IntegerField(default=1, null=False, blank=False)
	quinta = models.IntegerField(default=1, null=False, blank=False)
	sexta = models.CharField(max_length=250, null=True, blank=True)
	septima = models.CharField(max_length=250, null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.datetime.now())