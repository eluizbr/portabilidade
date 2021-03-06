# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from celery import task
from django.conf import settings
from portabilidade.celery import app
from django.shortcuts import render,get_object_or_404
from django.db import IntegrityError
from django.http import HttpResponse
from port.models import Portados, NaoPortados, Cadastro, Cdr, Prefixo, PlanoCliente, Plano, Retorno, Cache, CspRetorno
from revenda.models import Comissao_revenda, Codigo_revenda
from post_office import mail
from pagseguro.api import PagSeguroItem, PagSeguroApi
from django.core.exceptions import ObjectDoesNotExist
import datetime
from datetime import timedelta,datetime,date

import decimal
import os

@task
def insert_cdr(request,numero):

	data = datetime.now()
	agora = data.strftime("%H:%M:%S")

	chave = request
	numero = numero
	tamanho = len(numero)
	portado = Portados.objects.values_list('numero').filter(numero=numero)

	if len(chave) == 8:

		z = Cadastro.objects.get(cod_cliente=chave)
		id_user = z.id
		cod_cliente = z.cod_cliente

	else:

		z = Cadastro.objects.get(chave=chave)
		id_user = z.id
		cod_cliente = z.cod_cliente

	x = PlanoCliente.objects.get(cliente_id=id_user)
	plano_id_cliente = x.plano
	consultas = x.consultas
	gratis = x.consultas_gratis
	ativo = int(x.cache)
	tempo = x.tempo
	tipo = x.tipo
	tipo = int(tipo)

	hora = data + timedelta(minutes=tempo)
	hora = hora.strftime("%H:%M:%S")

	y = Plano.objects.get(id=plano_id_cliente)
	valor_plano = y.valor_consulta
	valor_plano_2 = y.valor_consulta

	try:
		cache = Cache.objects.get(numero=numero)
		numero_cache = cache.numero
		hora_cache = str(cache.cache)
	except ObjectDoesNotExist:
		hora_cache = agora


	### INICIO Remover credito ###
	a = agora.replace(":", "")
	h = hora_cache.replace(":", "")
	
	if tipo == 1:

		if ativo == 1:
			
			if a > h:

				Cache.objects.filter(numero=numero).delete()
				valor_plano = valor_plano_2
				total_consultas = consultas - 1
			
			elif a < h:
				valor_plano = 0.00
			else:
				
				total_consultas = consultas
		else:
			valor_plano = valor_plano
			total_consultas = consultas - 1

	else:
		total_consultas = 0
	### FIM Remover credito ###

	if portado:
		portado = Portados.objects.values_list('rn1').filter(numero=numero)[0]
		portado = portado[0]

		if tamanho == 10:
			prefix = numero[0:6]
		elif tamanho == 11:
			prefix = numero[0:7]

		dados = Prefixo.objects.get(prefixo=prefix)
		ddd = dados.ddd
		prefixo = dados.prefixo
		cidade = dados.cidade
		estado = dados.estado
		operadora = dados.operadora
		tipo = dados.tipo
		rn1 = dados.rn1

		x = Prefixo.objects.values('rn1','operadora').filter(rn1=portado).distinct()
		#print ddd,prefixo,cidade,estado,operadora,tipo,rn1

		for z in x:
			rn1 = z['rn1']
			operadora = z['operadora']
			retorno = CspRetorno.objects.values_list('retorno').filter(csp=rn1)

			try:
				retorno = retorno[0]
				retorno = retorno[0]
			except:
				retorno = rn1

			if len(chave) == 8:
				key = get_object_or_404(Cadastro, cod_cliente=chave)
			else:
				key = get_object_or_404(Cadastro, chave=chave)					
			
			### INICIO rotina CACHE - Só entra aqui se o cache esta hábilitado para o cliente ###
			if ativo == 1:
				try:
					Cache.objects.get(numero=numero)
				except Cache.DoesNotExist:
					Cache.objects.create(numero=numero,cache=hora,cliente=cod_cliente)
					total_consultas = consultas - 1
					PlanoCliente.objects.filter(cliente_id=id_user).update(consultas=total_consultas)
			### INICIO rotina CACHE - Só entra aqui se o cache esta hábilitado para o cliente ###
			elif ativo == 0:		
				total_consultas = consultas - 1
				PlanoCliente.objects.filter(cliente_id=id_user).update(consultas=total_consultas)

			Cdr.objects.create(cliente=key, numero=numero, prefixo=prefixo, ddd=ddd, rn1=rn1, retorno=retorno, operadora=operadora,\
										 cidade=cidade, estado=estado, tipo=tipo,portado=1,valor=valor_plano)

	else:

		if tamanho == 10:
			prefix = numero[0:6]
		elif tamanho == 11:
			prefix = numero[0:7]

		dados = Prefixo.objects.values('ddd','prefixo','cidade','estado','operadora','tipo', 'rn1').filter(prefixo=prefix)
		dados = Prefixo.objects.get(prefixo=prefix)
		ddd = dados.ddd
		
		prefixo = dados.prefixo
		cidade = dados.cidade
		estado = dados.estado
		operadora = dados.operadora
		tipo = dados.tipo
		rn1 = dados.rn1

		retorno = CspRetorno.objects.values_list('retorno').filter(csp=rn1)

		try:
			retorno = retorno[0]
			retorno = retorno[0]
		except:
			retorno = rn1

		if len(chave) == 8:
			key = get_object_or_404(Cadastro, cod_cliente=chave)
		else:
			key = get_object_or_404(Cadastro, chave=chave)	
		#print 'a chave e %s' %key		

		### INICIO rotina CACHE - Só entra aqui se o cache esta hábilitado para o cliente ###
		if ativo == 1:
			try:
				Cache.objects.get(numero=numero)
			except Cache.DoesNotExist:
				Cache.objects.create(numero=numero,cache=hora,cliente=cod_cliente)
				total_consultas = consultas - 1
				PlanoCliente.objects.filter(cliente_id=id_user).update(consultas=total_consultas)
		### INICIO rotina CACHE - Só entra aqui se o cache esta hábilitado para o cliente ###

		elif ativo == 0:
			total_consultas = consultas - 1
			PlanoCliente.objects.filter(cliente_id=id_user).update(consultas=total_consultas)

		Cdr.objects.create(cliente=key, numero=numero, prefixo=prefixo, ddd=ddd, rn1=rn1, retorno=retorno, operadora=operadora,\
									 cidade=cidade, estado=estado, tipo=tipo,portado=0,valor=valor_plano)

@task
def atualiza_compra(retorno):

	id_pagseguro = retorno.replace("-", "")
	pagseguro_api = PagSeguroApi()
	data = pagseguro_api.get_transaction(id_pagseguro)
	reference = data['transaction']['reference']

	cad = Cadastro.objects.get(cod_cliente=reference)
	user = cad.id
	nome = cad.nome
	usuario = cad.user_id
	email_cad = cad.email

	agora = datetime.now()

	try:

		r = Retorno.objects.get(code=id_pagseguro)
		retorno = str(r.code)
		unico = str(id_pagseguro)

		if retorno == unico:

			status_atual = Retorno.objects.values_list('status').filter(code=id_pagseguro)[0]
			status_atual = int(status_atual[0])
			status = data['transaction']['status']
			status = int(status)

			if status_atual !=  status:
				Retorno.objects.filter(code=retorno).update(lastEventDate=agora,status=status)

				if status == 3:
					atualiza_pago(id_pagseguro,usuario,status)

			else:
				### Atualiza da data da ultima consulta

				if status == 1:
					Retorno.objects.filter(code=retorno).update(lastEventDate=agora)

				if status == 2:

					mail.send(
					    [email_cad],
					    sender=settings.DEFAULT_FROM_EMAIL,
					    template='status_2',
					    context={'nome': nome},
					)
				if status == 7:

					mail.send(
					    [email_cad],
					    sender=settings.DEFAULT_FROM_EMAIL,
					    template='status_7',
					    context={'nome': nome},
					)

	except ObjectDoesNotExist:

		date = data['transaction']['date']
		lastEventDate = data['transaction']['lastEventDate']
		code = data['transaction']['code']
		code = code.replace("-", "")
		reference = data['transaction']['reference']
		status = data['transaction']['status']
		paymentMethod = data['transaction']['paymentMethod']['type']
		paymentMethodCode = data['transaction']['paymentMethod']['code']
		grossAmount = data['transaction']['grossAmount']
		discountAmount = data['transaction']['discountAmount']
		netAmount = data['transaction']['netAmount']
		extraAmount = data['transaction']['extraAmount']
		item = data['transaction']['items']['item']['description']
		id_plano = data['transaction']['items']['item']['id']
		name = data['transaction']['sender']['name']
		email = data['transaction']['sender']['email']
		areaCode = data['transaction']['sender']['phone']['areaCode']
		phone = data['transaction']['sender']['phone']['number']

		Retorno.objects.update_or_create(date=date,lastEventDate=lastEventDate,code=code,reference=reference,status=status,
								paymentMethod=paymentMethod,paymentMethodCode=paymentMethodCode,grossAmount=grossAmount,
								discountAmount=discountAmount,netAmount=netAmount,extraAmount=extraAmount,item=item,id_plano=id_plano,
								name=name,email=email,phone=areaCode+phone,cliente_id=user)
		mail.send(
		    [email_cad],
		    sender=settings.DEFAULT_FROM_EMAIL,
		    template='status_1',
		    context={'nome': name},
		)
		
		status = int(status)

		if status == 2:

			mail.send(
			    [email_cad],
			    sender=settings.DEFAULT_FROM_EMAIL,
			    template='status_2',
			    context={'nome': name},
			)

		if status == 3:
			atualiza_pago(id_pagseguro,usuario,status)


def atualiza_pago(id_pagseguro,usuario,status):


	u = Cadastro.objects.get(user_id=usuario)
	cad_user = u.id
	agora = datetime.now()
	pega_plano_cadastro = Cadastro.objects.values_list('plano').filter(id=cad_user)[0]
	pega_plano_cadastro = pega_plano_cadastro[0]

	#print compra['redirect_url']
	### INICIO Pega o valor do plano e o valor por consulta de obtem a quantidade de consultas
	x = Plano.objects.get(id=pega_plano_cadastro)
	id_plano = x.id
	descricao = x.plano
	valorD = x.valor
	valor = int(x.valor)
	v_consulta = x.valor_consulta

	try:
		result = valor / v_consulta
		result = decimal.Decimal(result)
	except ZeroDivisionError:
		result = 00.00
	## FIM Pega o valor do plano e o valor por consulta de obtem a quantidade de consultas
	p = PlanoCliente.objects.get(cliente_id=cad_user)
	pega_plano_cliente = p.plano

	# try:
	# 	### INICIO cria o plano baseado no retorno do PagSeguro ###
	# 	x = PlanoCliente.objects.get(cliente_id=cad_user)
	# 	user = x.id
	# 	print 'o user e %s' %user
	# 	PlanoCliente.objects.update(id=user,cliente_id=user,plano=pega_plano_cliente,consultas=result,consultas_gratis=0)
	# 	### FIM cria o plano baseado no retorno do PagSeguro ###

	# except IntegrityError:
	# Pega o plano no cadastro do cliente
	p = Cadastro.objects.get(user_id=cad_user)
	plano = p.plano
	nome = p.first_name
	email = p.email
	revenda_id = p.cod_revenda
	cliente_id = p.id
	login = p.login
	

	# ID da revenda
	rev = Codigo_revenda.objects.get(revenda=revenda_id)
	codigo_revenda = rev.revenda


	# Pega o plano comprado
	d = Retorno.objects.get(code=id_pagseguro)
	retorno_id = d.id
	plano_id = d.id_plano
	code = d.code
	reference = d.reference
	data = d.date
	nome = d.name
	email_C = d.email
	phone = d.phone
	valor_R = d.grossAmount + d.extraAmount
	comissao = d.grossAmount / 10

	b = PlanoCliente.objects.get(cliente_id=cad_user)
	b = b.plano

	if b != plano:
		PlanoCliente.objects.filter(plano=b).update(plano=plano)
		b = PlanoCliente.objects.get(cliente_id=cad_user)
		b = b.plano


	x = PlanoCliente.objects.get(cliente_id=cad_user)
	id_plano = x.id
	consultas = int(x.consultas)

	z = Plano.objects.get(id=plano_id)
	valor = int(z.valor)
	nome_plano = z.plano
	valor_consulta = z.valor_consulta
	gratis = z.consultas_gratis
	results = int(valor / valor_consulta)

	controle = Retorno.objects.values_list('controle').filter(code=id_pagseguro)[0]
	controle = controle[0]

	if controle == 0:

		novo_saldo = consultas + results + gratis
		PlanoCliente.objects.filter(cliente_id=cad_user).update(consultas=novo_saldo,plano=plano_id,nome_plano=descricao)
		Retorno.objects.filter(code=id_pagseguro).update(controle=1,consultas=results,lastEventDate=agora,status=status)
		Cadastro.objects.filter(id=cad_user).update(plano=plano_id)

		# Insere a comissao
		Comissao_revenda.objects.create(login=login,nome=nome,revenda=codigo_revenda,data_compra=data,comissao=comissao,retorno_id=retorno_id)

		mail.send(
		    [email],
		    sender=settings.DEFAULT_FROM_EMAIL,
		    template='status_3',
		    context={'nome': nome,'consultas': results, 'code':code,'reference':reference,'data':data,
				    'nome':nome,'valor_R':valor_R,'nome_plano':nome_plano,'results':results,'email_C':email_C,'phone':phone},
		)

@task
def procura():

	x = Retorno.objects.values_list('code').filter(status=1)
	for v in x:
		code = v[0]
		atualiza_compra(code)

@task
def limpa_cache():

	data = datetime.now()

	hora_1 = data - timedelta(hours=2)
	hora_2 = data - timedelta(hours=1)

	inicio = hora_1.strftime("%H:%M:%S")
	fim = hora_2.strftime("%H:%M:%S")

	Cache.objects.filter(cache__range=(inicio,fim)).delete()

@task
def email():

	os.system('/Volumes/DADOS/email.sh')
