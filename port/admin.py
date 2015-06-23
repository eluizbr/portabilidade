from django.contrib import admin
from .models import AuthKey,Cadastro

class AuthKeyAdmin(admin.ModelAdmin):
	list_display = ['nome', 'chave']


class CadastroAdmin(admin.ModelAdmin):
	list_display = ['user']

admin.site.register(AuthKey,AuthKeyAdmin)
admin.site.register(Cadastro,CadastroAdmin)



