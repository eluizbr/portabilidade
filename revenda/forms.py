# -*- coding: UTF-8 -*-
from django import forms
from port.models import Cadastro
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import random
from port.validar_cpf import CPF


class RevendaForm(forms.ModelForm):

	class Meta:
		model = Cadastro
		fields = '__all__'
		exclude = ['user','senha','revenda','cod_cliente','plano','cache','cod_revenda']

	def clean_cpf(self):
		if CPF(self.data['cpf']).isValid():
		    return self.data['cpf']
		else:
		    raise forms.ValidationError("CPF Invalido")