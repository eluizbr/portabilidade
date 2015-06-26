# -*- coding: UTF-8 -*-

from django.shortcuts import redirect, HttpResponseRedirect, render
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from django.conf import settings
from pagseguro.api import PagSeguroItem, PagSeguroApi
from pagseguro.signals import checkout_realizado
from models import Retorno, Cadastro
from datetime import datetime

# z = PlanoCliente.objects.get(cliente=request.user.id)
	# print 'saldo atual é %s' %z.consultas
	# z.plano = pega_plano_cadastro
	# z.consultas = z.consultas + result
	# z.save()
	# print 'saldo atual é %s' %z.consultas

# #print compra['redirect_url']
# ### INIICIO Pega o valor do plano e o valor por consulta de obtem a quantidade de consultas
# x = Plano.objects.get(id=pega_plano_cadastro)
# id_plano = x.id
# print id_plano
# descricao = x.plano
# valorD = x.valor
# print valorD
# valor = int(x.valor)
# v_consulta = x.valor_consulta
# try:
# 	result = valor / v_consulta
# 	print result
# 	result = decimal.Decimal(result)
# except ZeroDivisionError:
# 	result = 00.00
### FIM Pega o valor do plano e o valor por consulta de obtem a quantidade de consultas

def pagseguro(id,descricao,valor,codigo):

	compra = PagSeguroItem(id=id, description=descricao, amount=valor,quantity=1)

	pagseguro_api = PagSeguroApi(reference=codigo)
	pagseguro_api.add_item(compra)
	data = pagseguro_api.checkout()
	url = data['redirect_url']

	return url

#http://eluizbr.asuscomm.com:8000/portabilidade/retorno/?id_pagseguro=36053808D9A64EFB942131A7B02C15F5
def registra_compra(id_pagseguro):
	
	pagseguro_api = PagSeguroApi()
	data = pagseguro_api.get_transaction(id_pagseguro)

	print id_pagseguro
	id_pagseguro = id_pagseguro.replace("-", "")
	agora = datetime.now()
	print agora

	try:

		retorno = Retorno.objects.values_list('code').filter(code=id_pagseguro)[0]
		retorno = retorno[0]
		unico = str(id_pagseguro)

		if retorno == unico:

			status_atual = Retorno.objects.values_list('status').filter(code=id_pagseguro)[0]
			status_atual = int(status_atual[0])
			print type(status_atual)
			status = data['transaction']['status']
			status = int(status)
			print type(status)

			if status_atual !=  status:

				print 'é diferente'
				Retorno.objects.filter(code=retorno).update(lastEventDate=agora,status=status)
			else:
				print 'é igual'
				### Atualiza da data da ultima consulta
				if status == 1:
					Retorno.objects.filter(code=retorno).update(lastEventDate=agora)


	except IndexError:


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

		Retorno.objects.create(date=date,lastEventDate=lastEventDate,code=code,reference=reference,status=status,
								paymentMethod=paymentMethod,paymentMethodCode=paymentMethodCode,grossAmount=grossAmount,
								discountAmount=discountAmount,netAmount=netAmount,extraAmount=extraAmount,item=item)

	




		#return HttpResponseRedirect('/portabilidade/meus-dados/') 
	