from django.contrib import admin
from .models import Cadastro, Plano, PlanoCliente

class PlanoAdmin(admin.ModelAdmin):
	list_display = ['plano','descricao','valor','valor_consulta', 'consultas_gratis']

class PlanoClienteAdmin(admin.ModelAdmin):
	list_display = ['cliente','plano','consultas','consultas_gratis']


class CadastroAdmin(admin.ModelAdmin):
	list_display = ['user']


admin.site.register(Plano,PlanoAdmin)
admin.site.register(PlanoCliente,PlanoClienteAdmin)
admin.site.register(Cadastro,CadastroAdmin)
