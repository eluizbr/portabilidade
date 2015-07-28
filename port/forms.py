# -*- coding: UTF-8 -*-
from django import forms
from models import Cadastro, Plano, PlanoCliente
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import random
from validar_cpf import CPF

class CadastroForm(forms.ModelForm):


	class Meta:
		model = Cadastro
		fields = '__all__'
		exclude = ['user','cod_cliente','consultas','plano','cache']

	def clean_cpf(self):
		print "CLEAN CPF"
		if CPF(self.data['cpf']).isValid():
		    return self.data['cpf']
		else:
		    raise forms.ValidationError("Invalid CPF")


class CompraFrom(forms.ModelForm):

	class Meta:
		model = Plano
		fields = '__all__'
		exclude = ['consultas_gratis','taxas','tipo']

class PlanoClienteForm(forms.ModelForm):

	class Meta:
		model = PlanoCliente
		fields = ['ddd', 'aviso_email','saldo_baixo','sem_saldo','aviso_saldo']