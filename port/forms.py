from django import forms
from models import Cadastro
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import random

class CadastroForm(forms.ModelForm):


	class Meta:
		model = Cadastro
		fields = '__all__'
		exclude = ['user','cod_cliente', 'plano']
