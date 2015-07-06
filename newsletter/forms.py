# -*- coding: UTF-8 -*-
from django import forms
from models import envio

class EnvioForm(forms.ModelForm):

	class Meta:
		model = envio
		fields = '__all__'
		exclude = ['data','enviado']



