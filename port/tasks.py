# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from celery import task

from portabilidade.celery import app
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from port.models import Portados, NaoPortados, AuthKey, Cdr, Prefixo

@task
def insert_cdr(request,numero):

	chave = request
	numero = numero
	tamanho = len(numero)
	portado = Portados.objects.values_list('numero').filter(numero=numero)

	if portado:
		portado = Portados.objects.values_list('rn1').filter(numero=numero)

		if tamanho == 10:
			prefix = numero[0:6]
		elif tamanho == 11:
			prefix = numero[0:7]

		dados = Prefixo.objects.values('ddd','prefixo','cidade','estado','operadora','tipo', 'rn1').filter(prefixo=prefix)

		for item in dados:
			ddd = item['ddd']
			prefixo = item['prefixo']
			cidade = item['cidade']
			estado = item['estado']
			operadora = item['operadora']
			tipo = item['tipo']
			rn1 = item['rn1']

			key = get_object_or_404(AuthKey, chave=chave)		
			criar = Cdr.objects.create(cliente=key, numero=numero, prefixo=prefixo, ddd=ddd, rn1=rn1, operadora=operadora,\
										 cidade=cidade, estado=estado, tipo=tipo,portado=1)
			criar.save()

			print key,estado,cidade,operadora,tipo
	else:

		if tamanho == 10:
			prefix = numero[0:6]
		elif tamanho == 11:
			prefix = numero[0:7]

		dados = Prefixo.objects.values('ddd','prefixo','cidade','estado','operadora','tipo', 'rn1').filter(prefixo=prefix)

		for item in dados:
			ddd = item['ddd']
			prefixo = item['prefixo']
			cidade = item['cidade']
			estado = item['estado']
			operadora = item['operadora']
			tipo = item['tipo']
			rn1 = item['rn1']

			key = get_object_or_404(AuthKey, chave=chave)		
			criar = Cdr.objects.create(cliente=key, numero=numero, prefixo=prefixo, ddd=ddd, rn1=rn1, operadora=operadora,\
										 cidade=cidade, estado=estado, tipo=tipo)
			criar.save()
			

			print key,estado,cidade,operadora,tipo
