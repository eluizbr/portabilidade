# -*- coding: UTF-8 -*-

from django.shortcuts import redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from django.conf import settings
from pagseguro.api import PagSeguroItem, PagSeguroApi
from pagseguro.signals import checkout_realizado

def load_signal(sender, data, **kwargs):
	print(data['success'])


def pagseguro(id,descricao,valor):

	compra = PagSeguroItem(id=id, description=descricao, amount=valor,quantity=1)
	
	pagseguro_api = PagSeguroApi(reference='563dd4b8f3d740fe80a50058dc5cf938')
	pagseguro_api.add_item(compra)
	data = pagseguro_api.checkout()
	#print data['redirect_url']
	url = data['redirect_url']
	#print url
	
	return url
	#print data['transaction']['code']
	#checkout_realizado.connect(load_signal)

#pagseguro('001','Teste','100.00')

	