from django.contrib import admin

from .models import envio

class envioAdmin(admin.ModelAdmin):

	list_display = ['nome']


admin.site.register(envio,envioAdmin)
