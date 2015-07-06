# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.

class envio(models.Model):
	nome = models.CharField(max_length=255)
	telefone = models.CharField(max_length=25,default='(00)0000-0000')
	email = models.EmailField()
	empresa = models.CharField(max_length=255)
	data = models.DateTimeField(auto_now_add=True)
	enviado = models.IntegerField(default=0)
