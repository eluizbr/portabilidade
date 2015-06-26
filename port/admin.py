from django.contrib import admin
from .models import Cadastro, Plano, PlanoCliente, Retorno

class PlanoAdmin(admin.ModelAdmin):
	list_display = ['plano','descricao','valor','valor_consulta', 'consultas_gratis']

class PlanoClienteAdmin(admin.ModelAdmin):
	list_display = ['cliente','consultas','consultas_gratis']


class CadastroAdmin(admin.ModelAdmin):
	list_display = ['user']


class RetornoAdmin(admin.ModelAdmin):
	list_display = ['date','lastEventDate','code','reference','status','paymentMethod','paymentMethodCode',
					'grossAmount','discountAmount','netAmount','extraAmount','item']

admin.site.register(Plano,PlanoAdmin)
admin.site.register(PlanoCliente,PlanoClienteAdmin)
admin.site.register(Cadastro,CadastroAdmin)
admin.site.register(Retorno,RetornoAdmin)
