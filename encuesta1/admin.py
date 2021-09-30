from django.contrib import admin

# Register your models here.

from . models import EncuestaModel


class EncuestaAdmin(admin.ModelAdmin):
	list_display = [ 'categoria', 'adscripcion', 'turno', 'sexo', 'antiguedad']
	search_fields = ['adscripcion']
	exclude = ('created_at',)



admin.site.register(EncuestaModel, EncuestaAdmin)