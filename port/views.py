# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from models import Portados, NaoPortados, Cdr, Prefixo, PlanoCliente
from ratelimit.decorators import ratelimit
from tasks import insert_cdr
from django.conf import settings
import MySQLdb
from django.db import connection
import datetime
import random
from datetime import timedelta,date
from forms import CadastroForm
from models import Cadastro, Plano
from django.contrib.auth.models import User
#from celery import signature

@login_required
def index(request):

	return render(request, 'index.html')

@login_required
def meus_dados(request):

	user = User.objects.get(pk=request.user.id)
	id_cliente = Cadastro.objects.values('plano').filter(user_id=request.user.id)

	try:
		plano = PlanoCliente.objects.values_list('plano_id').filter(id=id_cliente)[0]
		plano = plano[0]

	except IndexError:
		plano = 1

	try:
		cad = Cadastro.objects.get(user=user)
		cod_cliente = cad.chave

		if request.method == 'POST':
			form = CadastroForm(request.POST or None, instance=cad)
			
			if form.is_valid():
				obj = form.save(commit=False)
				obj.email = user.email
				obj.user = user
				obj.cod_cliente = int(random.randint(10000000, 99000000))
				obj.save()

				pega_plano_cadastro = Cadastro.objects.values_list('plano_id').filter(plano_id=id_cliente)[0]
				pega_plano_cadastro = pega_plano_cadastro[0]
				print pega_plano_cadastro

				pega_plano_cliente = PlanoCliente.objects.values_list('plano_id').filter(id=request.user.id)[0]
				pega_plano_cliente = pega_plano_cliente[0]
				print pega_plano_cliente

				if pega_plano_cliente != pega_plano_cadastro:
					print u'plano são diferentes'

					### INIICIO Pega o valor do plano e o valor por consulta de obtem a quantidade de consultas
					x = Plano.objects.get(id=pega_plano_cadastro)
					valor = x.valor
					v_consulta = x.valor_consulta
					try:
						result = valor / v_consulta
					except ZeroDivisionError:
						result = 0

					print int(result)
					### FIM Pega o valor do plano e o valor por consulta de obtem a quantidade de consultas

					z = PlanoCliente.objects.get(plano_id=pega_plano_cliente)
					print 'saldo atual é %s' %z.consultas
					print z
					z.plano_id = pega_plano_cadastro
					z.consultas = z.consultas + result
					z.save()
					print 'saldo atual é %s' %z.consultas
				else:
					print u'planos são iguais'
					#obj.save()
		else:

			form = CadastroForm(instance=cad)
		return render(request, 'meus_dados.html', locals())
	
	except Cadastro.DoesNotExist:
		
		cad = user

	if request.method == 'POST':
		form = CadastroForm(request.POST)
		
		if form.is_valid():
			obj = form.save(commit=False)
			obj.email = user.email
			obj.user = user
			obj.cod_cliente = int(random.randint(10000000, 99000000))
			obj.save()
	else:

		form = CadastroForm(instance=cad)

	return render(request, 'meus_dados.html', locals())


@login_required
def operadoras(request):

	## Conexão ao banco MySQL
	try:
		c = connection.cursor()
		
		id_cliente = Cadastro.objects.values_list('id').filter(user_id=request.user.id)[0]
		plano = PlanoCliente.objects.values_list('consultas').filter(cliente_id=request.user.id)
		operadoras = Cdr.objects.values('operadora','tipo').order_by('operadora').annotate(Count('cidade')).filter(cliente=id_cliente)
		tipo_numero = Cdr.objects.values('tipo').annotate(Count('tipo')).filter(cliente=id_cliente)
		ultimos_numero = operadoras = Cdr.objects.values('numero','operadora','tipo','data_hora').order_by('-id').filter(cliente=id_cliente)[:5][::1]

		try:

			id_cliente = id_cliente[0]
			consultas = PlanoCliente.objects.values_list('consultas').filter(cliente_id=id_cliente)[0]
			consultas = consultas[0]

		except ZeroDivisionError:
			
			consultas = 0
		
		data = date.today()
		ontem_d = data - timedelta(days=1)
		ontem_d = ontem_d.strftime('%d')
		hoje = data.strftime('%d')
		mes_atual = data.strftime('%m')
		week_hoje = date.today()
		week = date.today() - timedelta(days=7)

		nao_portado_ontem = Cdr.objects.filter(data__day=ontem_d,portado=0,cliente=id_cliente).count()
		nao_portado_dia = Cdr.objects.filter(data__day=hoje,portado=0,cliente=id_cliente).count()
		nao_portado_semana = Cdr.objects.filter(data__range=(week ,week_hoje),portado=0,cliente=id_cliente).count()
		
		nao_portado_mes = Cdr.objects.filter(data__month=mes_atual,portado=0,cliente=id_cliente).count()

		portados_dia = Cdr.objects.filter(data__day=hoje,portado=1,cliente=id_cliente).count()
		portados_ontem = Cdr.objects.filter(data__day=ontem_d,portado=1,cliente=id_cliente).count()
		portados_semana = Cdr.objects.filter(data__range=(week, week_hoje),portado=1,cliente=id_cliente).count()
		portados_mes = Cdr.objects.filter(data__month=mes_atual,portado=1,cliente=id_cliente).count()

		portado_diff = [portados_ontem,portados_dia]

		for a, b in zip(portado_diff[::1], portado_diff[1::1]):
		    try:
		    
		    	portado_diff = 100 * (b - a) / a
		    
		    except ZeroDivisionError:
		    
		    	portado_diff = 0

		nao_portado_diff = [nao_portado_ontem,nao_portado_dia]

		for a, b in zip(nao_portado_diff[::1], nao_portado_diff[1::1]):
		    try:
		    	
		    	nao_portado_diff = 100 * (b - a) / a
		    
		    except ZeroDivisionError:
		    	
		    	nao_portado_diff = 0


		total ="""SELECT DISTINCT operadora,
						  COUNT( IF( tipo='FIXO', 1, NULL ) ) AS fixo,
						  COUNT( IF( tipo='MOVEL', 1, NULL ) ) AS movel,
						  COUNT( IF( tipo='RADIO', 1, NULL ) ) AS radio
						FROM port_cdr WHERE cliente_id = %d
						GROUP BY operadora""" % id_cliente
		total = c.execute(total)
		total = c.fetchall()

		cidades = """SELECT DISTINCT SQL_CALC_FOUND_ROWS cidade
						FROM port_cdr WHERE cliente_id = %d """ % id_cliente
		cidades = c.execute(cidades)
		cidades = c.fetchone()
		cidades = 'SELECT FOUND_ROWS() as total'
		cidades = c.execute(cidades)
		cidades = c.fetchone()[0]

		estados = """SELECT DISTINCT SQL_CALC_FOUND_ROWS estado
						FROM port_cdr WHERE cliente_id = %d """ % id_cliente
		estados = c.execute(estados)
		estados = c.fetchone()
		estados = 'SELECT FOUND_ROWS() as total'
		estados = c.execute(estados)
		estados = c.fetchone()[0]


		total_consultas = Cdr.objects.all().count()

		# teste2 = teste.filter(cidade='Belo Horizonte')
		
		portados = Cdr.objects.values('portado').annotate(cnt=Count('portado')).order_by('portado')
		total_items = Cdr.objects.count()
		total_items = float(total_items)

		items = [
	        {'portados': g['portado'], 'value': g['cnt'] * 100 / total_items} for g in portados
	    ]
		return render(request, 'operadoras.html', locals())
	
	except IndexError:
		return redirect('/portabilidade/meus-dados/')


#@ratelimit(key='ip', rate='60/m', block=True)
def consulta(request,numero):

	segredo = request.GET['key']
	segredo = str(segredo)

	insert_cdr.apply_async(kwargs={'request': segredo, 'numero': numero},countdown=1)
	rn1 = len(numero)

	try:

		key = request.GET['key']
		key = str(key)

		chave = Cadastro.objects.values_list('chave').filter(chave=key)[0]
		chave = chave[0]
		chave = str(chave)


		if key == chave:

			if rn1 == 9:

				rn1 = Portados.objects.values_list('rn1').filter(numero=numero)
				rn1 = str(rn1)[5:7]

				if not rn1:
					rn1 = str(numero)[0:6]
					rn1 = NaoPortados.objects.values_list('rn1').filter(prefixo=rn1)
					rn1 = str(rn1)[5:7]

			elif rn1 == 10:
				rn1 = Portados.objects.values_list('rn1').filter(numero=numero)
				rn1 = str(rn1)[5:7]

				if not rn1:
					rn1 = str(numero)[0:6]
					rn1 = NaoPortados.objects.values_list('rn1').filter(prefixo=rn1)
					rn1 = str(rn1)[5:7]

			elif rn1 == 11:
				rn1 = Portados.objects.values_list('rn1').filter(numero=numero)
				rn1 = str(rn1)[5:7]

				if not rn1:
					rn1 = str(numero)[0:7]
					rn1 = NaoPortados.objects.values_list('rn1').filter(prefixo=rn1)
					rn1 = str(rn1)[5:7]
			
			elif rn1 <= 10:
			
				rn1 = 0
				response = HttpResponse(rn1, content_type='text/plain')
				return response			

			response = HttpResponse(rn1, content_type='text/plain')
			return response
		else:

			rn1 = 0
			response = HttpResponse(rn1, content_type='text/plain')
			return response
	except:

		rn1 = 0
		response = HttpResponse(rn1, content_type='text/plain')
		return response


