# -*- coding: UTF-8 -*-

from django.shortcuts import redirect, HttpResponseRedirect, render
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from django.conf import settings
from pagseguro.api import PagSeguroItem, PagSeguroApi
from pagseguro.signals import checkout_realizado
from models import Retorno, Cadastro, PlanoCliente, Plano
from datetime import datetime
import decimal
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from post_office import mail


def pagseguro(id,descricao,valor,codigo,taxa):
	print id,descricao,valor,codigo

	compra = PagSeguroItem(id=id,description=descricao,amount=valor,quantity=1)

	pagseguro_api = PagSeguroApi(reference=codigo,extraAmount=taxa)
	pagseguro_api.add_item(compra)
	data = pagseguro_api.checkout()
	url = data['redirect_url']

	return url

#http://eluizbr.asuscomm.com:8000/portabilidade/retorno/?id_pagseguro=36053808D9A64EFB942131A7B02C15F5
def registra_compra(id_pagseguro,usuario):
	
	print usuario
	u = Cadastro.objects.get(id=usuario)
	user = u.id
	print 'o usuario é %s' %user
	pagseguro_api = PagSeguroApi()
	data = pagseguro_api.get_transaction(id_pagseguro)
	id_pagseguro = id_pagseguro.replace("-", "")
	agora = datetime.now()

	try:

		r = Retorno.objects.get(code=id_pagseguro)
		retorno = str(r.code)
		print type(retorno)
		unico = str(id_pagseguro)
		print type(unico)

		if retorno == unico:

			status_atual = Retorno.objects.values_list('status').filter(code=id_pagseguro)[0]
			status_atual = int(status_atual[0])
			status = data['transaction']['status']
			status = int(status)

			if status_atual !=  status:

				print 'é diferente'
				Retorno.objects.filter(code=retorno).update(lastEventDate=agora,status=status)

				if status == 3:
					atualiza_pago(id_pagseguro,usuario,status)

			else:
				print 'é igual'
				### Atualiza da data da ultima consulta
				if status == 1:
					Retorno.objects.filter(code=retorno).update(lastEventDate=agora)


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

		Retorno.objects.create(date=date,lastEventDate=lastEventDate,code=code,reference=reference,status=status,
								paymentMethod=paymentMethod,paymentMethodCode=paymentMethodCode,grossAmount=grossAmount,
								discountAmount=discountAmount,netAmount=netAmount,extraAmount=extraAmount,item=item,id_plano=id_plano,
								name=name,email=email,phone=areaCode+phone)
		
		status = int(status)

		if status == 3:
			atualiza_pago(id_pagseguro,usuario,status)


def atualiza_pago(id_pagseguro,usuario,status):

	u = Cadastro.objects.get(user_id=usuario)
	user = u.id
	print user
	agora = datetime.now()
	pega_plano_cadastro = Cadastro.objects.values_list('plano').filter(id=user)[0]
	pega_plano_cadastro = pega_plano_cadastro[0]
	print 'o plano cadastrado é %s' %pega_plano_cadastro

	#print compra['redirect_url']
	### INIICIO Pega o valor do plano e o valor por consulta de obtem a quantidade de consultas
	x = Plano.objects.get(id=pega_plano_cadastro)
	id_plano = x.id
	print id_plano
	descricao = x.plano
	valorD = x.valor
	print valorD
	valor = int(x.valor)
	v_consulta = x.valor_consulta
	try:
		result = valor / v_consulta
		print result
		result = decimal.Decimal(result)
	except ZeroDivisionError:
		result = 00.00
	## FIM Pega o valor do plano e o valor por consulta de obtem a quantidade de consultas
	print user
	p = PlanoCliente.objects.get(cliente=user)
	pega_plano_cliente = p.plano
	print 'plano é %s' %pega_plano_cliente

	try:
		### INICIO cria o plano baseado no retorno do PagSeguro ###
		PlanoCliente.objects.create(cliente=user,plano=pega_plano_cliente,consultas=result,consultas_gratis=0)
		### FIM cria o plano baseado no retorno do PagSeguro ###

	except IntegrityError:
		
		print 'ja tem <--------'
		# Pega o plano no cadastro do cliente
		p = Cadastro.objects.get(id=user)
		plano = p.plano
		nome = p.first_name
		email = p.email
		print 'Cadastro %s' %p
		
		# Pega o plano comprado
		d = Retorno.objects.get(code=id_pagseguro)
		plano_id = d.id_plano
		code = d.code
		print 'Plano contratado %s' %plano_id

		b = PlanoCliente.objects.get(cliente=user)
		b = b.plano
		print 'PlanoCliente %s' %b

		if b != p:
			print 'planos sao diferentes'
			PlanoCliente.objects.filter(plano=b).update(plano=plano)
			b = PlanoCliente.objects.get(cliente=user)
			b = b.plano
			print 

		x = PlanoCliente.objects.get(cliente=user)
		id_plano = x.id
		print id_plano
		consultas = int(x.consultas)
		print 'saldo atual é %s' %(consultas)


		z = Plano.objects.get(id=plano_id)
		valor = int(z.valor)
		print valor
		valor_consulta = z.valor_consulta
		print valor_consulta
		gratis = z.consultas_gratis
		results = int(valor / valor_consulta)
		print 'saldo a ser somado é %s' %(results)

		controle = Retorno.objects.values_list('controle').filter(code=id_pagseguro)[0]
		controle = controle[0]
		print controle

		if controle == 0:

			novo_saldo = consultas + results + gratis
			print 'o novo saldo é %s' %novo_saldo
			PlanoCliente.objects.filter(cliente=user).update(consultas=novo_saldo,plano=plano_id,nome_plano=descricao)
			Retorno.objects.filter(code=id_pagseguro).update(controle=1,consultas=results,lastEventDate=agora,status=status)
			Cadastro.objects.filter(id=user).update(plano=plano_id)

			mail.send(
			    [email],
			    sender=settings.DEFAULT_FROM_EMAIL,
			    template='status_3',
			    context={'nome': nome,'consultas': results, 'code':code},
			)

