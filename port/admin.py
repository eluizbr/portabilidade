from django.contrib import admin
from .models import Cadastro, Plano

class PlanoAdmin(admin.ModelAdmin):
	list_display = ['plano','valor','valor_consulta', 'consultas_gratis']


class CadastroAdmin(admin.ModelAdmin):
	list_display = ['user']


admin.site.register(Plano,PlanoAdmin)
admin.site.register(Cadastro,CadastroAdmin)

