# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from port.models import Cadastro, Retorno
from datetime import datetime

today = datetime.today()
mes = today.month
ano = today.year


class Codigo_revenda(models.Model):
    revenda = models.CharField(u'Codigo da Revenda',max_length=100, unique=True, default=0)
    cliente = models.ForeignKey(Cadastro)

class Comissao_revenda(models.Model):
	login = models.CharField(u'Login do Cliente',max_length=100)
	nome = models.CharField(u'Nome do Cliente',max_length=100)
	revenda = models.CharField(u'Codigo da Revenda',max_length=100)
	retorno = models.ForeignKey(Retorno)
	data_compra = models.DateTimeField(auto_now=False)
	comissao = models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2, default=00.00)
	mes = models.IntegerField(blank=True, null=True, default=mes)
	ano = models.IntegerField(blank=True, null=True, default=ano)

	def __unicode__(self):
		return unicode(self.login)
