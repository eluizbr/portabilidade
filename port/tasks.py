# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from celery import task

from portabilidade.celery import app
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from port.models import Portados, NaoPortados, Cadastro, Cdr, Prefixo, PlanoCliente, Plano

@task
def insert_cdr(request,numero):

	chave = request
	numero = numero
	tamanho = len(numero)
	portado = Portados.objects.values_list('numero').filter(numero=numero)

	z = Cadastro.objects.get(chave=chave)
	id_user = z.id
	print id_user

	x = PlanoCliente.objects.get(cliente=id_user)
	plano_id_cliente = x.plano
	print 'o ID do plano e %s' %plano_id_cliente 
	consultas = x.consultas
	print 'consultas restantes %s' %consultas
	gratis = x.consultas_gratis
	print 'consultas gratis restantes %s' %gratis
	tipo = x.tipo
	tipo = int(tipo)
	print 'tipo de plano é %s' %tipo

	y = Plano.objects.get(id=plano_id_cliente)
	valor_plano = y.valor_consulta
	print 'o valor por consulta e %s' %valor_plano

	### INICIO Remover credito ###
	if tipo == 1:
		total_consultas = consultas - 1
		print 'restou apenas %s creditos' %total_consultas

	else:
		total_consultas = 0
		print 'restou apenas %s creditos' %total_consultas		
	### FIM Remover credito ###

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

			key = get_object_or_404(Cadastro, chave=chave)		
			Cdr.objects.create(cliente=key, numero=numero, prefixo=prefixo, ddd=ddd, rn1=rn1, operadora=operadora,\
										 cidade=cidade, estado=estado, tipo=tipo,portado=1,valor=valor_plano)

			PlanoCliente.objects.filter(cliente=id_user).update(consultas=total_consultas)

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

			key = get_object_or_404(Cadastro, chave=chave)
			#print 'a chave e %s' %key		
			Cdr.objects.create(cliente=key, numero=numero, prefixo=prefixo, ddd=ddd, rn1=rn1, operadora=operadora,\
										 cidade=cidade, estado=estado, tipo=tipo,valor=valor_plano)
			
			PlanoCliente.objects.filter(cliente=id_user).update(consultas=total_consultas)
			#print key,estado,cidade,operadora,tipo
