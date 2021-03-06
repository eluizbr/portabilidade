# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import RequestContext
from django.db.models import Count, Sum
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from models import Portados, NaoPortados, Cdr, Prefixo, PlanoCliente, Retorno, SipBuddies, Cache, Csp, CspRetorno, PortPlanoCodCliente
from revenda.models import Codigo_revenda
from ratelimit.decorators import ratelimit
from tasks import insert_cdr, atualiza_compra
from django.conf import settings
import MySQLdb
from django.db import connection
import datetime
import random
import uuid
import decimal
from datetime import timedelta,date
from forms import CadastroForm, CompraFrom, PlanoClienteForm, CspRetornoFrom
from models import Cadastro, Plano, Retorno
from django.contrib.auth.models import User
from pagseguro.api import PagSeguroItem, PagSeguroApi
import compra
from post_office import mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
import funcoes

@csrf_exempt
def contato(request):
    name = request.POST.get('name', '')
    parceiro = request.POST.get('parceiro', '')
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    if name and message and email:

		mail.send(
		    ['eluizbr@gmail.com'],
		    sender=settings.DEFAULT_FROM_EMAIL,
		    template='contato',
		    context={'name':name,'subject':subject, 'message':message, 'email':email, 'phone':phone},
		)
		return redirect('http://cdr-port.net')

    elif parceiro and message and email:

		mail.send(
		    ['eluizbr@gmail.com'],
		    sender=settings.DEFAULT_FROM_EMAIL,
		    template='parceiro',
		    context={'name':parceiro,'subject':subject, 'message':message, 'email':email, 'phone':phone},
		)
        	return redirect('http://parceiros.cdr-port.net')

    else:
        return HttpResponse("Preencha todos os campos.")

@login_required
def index(request):

	return redirect('operadoras')

@login_required
def padrao(request):

	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user=user)
	cod_user = cad.id
	chave_cod = cad.cod_cliente
	revenda = cad.revenda
	z = PlanoCliente.objects.all().filter(cliente_id=cod_user)
	plano = PlanoCliente.objects.get(cliente_id=cod_user)
	ddd = plano.ddd
	aviso = plano.aviso_email
	retorno = plano.retorno
	saldo_baixo = plano.saldo_baixo
	sem_saldo = plano.sem_saldo
	aviso_saldo = plano.aviso_saldo
	#print retorno, aviso, sem_saldo, saldo_baixo

	ddd_v = request.POST.get('ddd', '')
	aviso_v = request.POST.get('aviso_email', '')
	retorno_v = request.POST.get('retorno', '')
	sem_saldo_v = request.POST.get('sem_saldo', '')
	saldo_baixo_v = request.POST.get('saldo_baixo', '')
	aviso_saldo_v = request.POST.get('aviso_saldo', '')

	if aviso_saldo_v == '':
		aviso_saldo_v = 250

	if request.method == 'POST':
		form = PlanoClienteForm(request.POST , instance=plano)
			
		if form.is_valid():
			obj = form.save(commit=False)
			obj.ddd = ddd_v
			obj.aviso_email = aviso_v
			obj.retorno = retorno_v
			obj.saldo_baixo = saldo_baixo_v
			obj.sem_saldo = sem_saldo_v
			obj.aviso_saldo = aviso_saldo_v
			obj.save()

			return redirect('/portabilidade/padrao')
	else:

		form = PlanoClienteForm(instance=plano)

	return render(request, 'padrao.html', locals())

@login_required
def asterisk(request):

	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user=user)
	chave = cad.chave
	chave_cod = cad.cod_cliente
	cod_cliente = cad.cod_cliente
	revenda = cad.revenda

	asterisk = SipBuddies.objects.get(cliente=cod_cliente)
	ast_user = asterisk.name
	ast_pass = asterisk.secret

	return render(request, 'asterisk.html', locals())

@login_required
def csp_retorno(request):

	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user=user)
	chave = cad.chave
	chave_cod = cad.cod_cliente
	cod_cliente = cad.cod_cliente
	user_id = cad.id
	revenda = cad.revenda

	todos_csp = Csp.objects.all()

	x = CspRetorno.objects.all().filter(user=user_id)

	csp_v = request.POST.get('csp', '')
	retorno_v = request.POST.get('retorno', '')
	# apaga_v = request.POST.get('apaga', '0')

	#apagar = CspRetorno.objects.filter(id=apaga_v).delete()

	if request.method == 'POST':
		form = CspRetornoFrom(request.POST)
			
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = user_id
			obj.csp = csp_v
			obj.retorno = retorno_v
			obj.save()

			return redirect('/portabilidade/csp-retorno')
	else:

		form = CspRetornoFrom()

	return render(request, 'csp_retorno.html', locals())

@login_required
def csp_retorno_del(request,deletar):

	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user=user)
	chave = cad.chave
	chave_cod = cad.cod_cliente
	cod_cliente = cad.cod_cliente
	user_id = cad.id
	revenda = cad.revenda

	todos_csp = Csp.objects.all()
	x = CspRetorno.objects.all().filter(user=user_id)
	
	apagar = CspRetorno.objects.filter(id=deletar).delete()

	return redirect('/portabilidade/csp-retorno')

@login_required
def csp(request):

	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user=user)
	cod_user = cad.id
	chave_cod = cad.cod_cliente
	revenda = cad.revenda
	
	operadora = Prefixo.objects.values('rn1','operadora','tipo').distinct()

	paginator = Paginator(operadora, 15)
	page = request.GET.get('page')

	try:
		contacts = paginator.page(page)
	
	except PageNotAnInteger:
		contacts = paginator.page(1)

	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	return render(request, 'csp.html', locals())

@login_required
def financeiro_info(request,id):

    financeiro_info = Retorno.objects.all().filter(id=id)
    return render(request,'financeiro_info.html', locals())

@login_required
def financeiro(request):

	user = User.objects.get(pk=request.user.id)
	
	cad = Cadastro.objects.get(user=user)
	user_id = cad.id
	nome = cad.first_name
	email = cad.email
	codigo_cliente = cad.cod_cliente
	cod_cliente = cad.chave
	cod_plano = cad.plano
	id_cliente = cad.id
	chave_cod = cad.cod_cliente
	revenda = cad.revenda

	x = PlanoCliente.objects.get(cliente_id=user_id)
	plano_nome = x.nome_plano
	tipo = x.tipo
	consultas = x.consultas
	expira = x.expira_em
	id_plano = x.plano
	v = Plano.objects.get(id=id_plano)
	valor_plano = v.valor

	todos = Plano.objects.values_list('plano','valor','especial')
	planos_cliente = PortPlanoCodCliente.objects.all().filter(cadastro_id=id_cliente)

	retorno = Retorno.objects.all().filter(reference=codigo_cliente)
	
	if request.method == 'POST' and 'plano' in request.POST:

		form = CompraFrom(request.POST)
		if form.is_valid():
			selecao = form.cleaned_data.get('plano')
			qs = Plano.objects.get(plano=selecao)
			id_plano = qs.id
			planos = qs.plano
			descricao = qs.descricao
			valor = qs.valor
			taxa = qs.taxas
			valorD = float(valor)
			valor_consulta = qs.valor_consulta
			try:
				total = int(valorD / valor_consulta)
			except ZeroDivisionError:
				total = 0
			valor_total = valor + taxa

			consultas_gratis = qs.consultas_gratis
			tipo = qs.tipo

			if request.method == 'POST' and 'selecionar' in request.POST:
				pass
			if request.method == 'POST' and 'comprar' in request.POST:
				### INICIO PAGSEGURO ###
				compra.pagseguro(id_plano,descricao,valor,codigo_cliente,taxa)
				return redirect(compra.pagseguro(id_plano,descricao,valor,codigo_cliente,taxa))
				### FIM PAGSEGURO ###
	else:

		form = CompraFrom()

	return render(request, 'financeiro.html', locals())
	
@login_required
def criar_user(request):

	data = datetime.datetime.now()
	mes = data + timedelta(days=30)
	user = User.objects.get(pk=request.user.id)

	if request.method == 'POST':
		form = CadastroForm(request.POST)
		print form.errors
			
		if form.is_valid():
			print form.errors
			obj = form.save(commit=False)
			#obj.email = user.email
			obj.user = user
			obj.cod_cliente = int(random.randint(10000000, 99000000))
			obj.save()


			try:
				### Se o plano não exite, então cria...
				cad = Cadastro.objects.get(user=user)
				user_id = cad.id
				codigo_cliente = cad.cod_cliente
				name = cad.first_name
				phone = cad.telefoneF
				z = PlanoCliente.objects.get(cliente_id=user_id)
				cliente = z.cliente_id
				plano = z.plano
			except PlanoCliente.DoesNotExist:
				z = PlanoCliente(consultas=500,consultas_gratis=0,cliente_id=user_id,plano=1,nome_plano='500 Grátis',criado_em=data,expira_em=mes,tipo=1)
				z.save()

				secret = int(random.randint(10000000, 99000000))
				sip = SipBuddies(name=codigo_cliente,port=5060,secret=secret,regseconds=0,cliente=codigo_cliente)
				sip.save()	
				### Se o plano não exite, então cria...

				# Associando cliente a revenda
				revenda = str(uuid.uuid4().get_hex()[0:10])
				z = Codigo_revenda.objects.create(revenda=revenda,cliente_id=user_id)

				# mail.send(
				#     'eluizbr@gmail.com', # List of email addresses also accepted
				#     sender=settings.DEFAULT_FROM_EMAIL,
				#     template='usuario_novo',
				#     context={'name': name,'phone':phone}
				# )

			return redirect('/portabilidade/meus-dados/')
	else:

		form = CadastroForm()
		print form.errors

	return render(request, 'criar_user.html', locals())	

@login_required
def meus_dados(request):

	user = User.objects.get(pk=request.user.id)

	try:
		cad = Cadastro.objects.get(user=user)
		user_id = cad.id
		codigo_cliente = cad.cod_cliente
		cod_cliente = cad.chave
		name = cad.first_name
		chave_cod = cad.cod_cliente
		revenda = cad.revenda

	except Cadastro.DoesNotExist:
		return redirect('/portabilidade/criar-user/')
	
	if request.method == 'POST':
		form = CadastroForm(request.POST or None, instance=cad)
		
		try:
			p = Cadastro.objects.get(user_id=request.user.id)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.save()
			else:

				form = CadastroForm(instance=cad)

		except Cadastro.DoesNotExist:
			
			if form.is_valid():
				obj = form.save(commit=False)
				#obj.email = user.email
				obj.user = user
				obj.cod_cliente = int(random.randint(10000000, 99000000))
				obj.save()

				# Gera cliente SIP
				secret = int(random.randint(10000000, 99000000))
				print name,secret,codigo_cliente
				sip = SipBuddies(name=name,port=5060,secret=secret,cliente=cod_cliente)
				sip.save()

				try:
					### Se o plano não exite, então cria...
					z = PlanoCliente.objects.get(cliente_id=request.user.id)
				except PlanoCliente.DoesNotExist:
					z = PlanoCliente(consultas=0,consultas_gratis=0,cliente_id=user_id,plano=1,nome_plano='Sem Plano')
					z.save()
					### Se o plano não exite, então cria...
	else:

		form = CadastroForm(instance=cad)

	return render(request, 'meus_dados.html', locals())

@login_required
def cdr(request):

	hora = datetime.datetime.now()
	hoje = hora.strftime("%Y-%m-%dT23:59:59") 
	ontem = hora - timedelta(days=1)
	ontem = ontem.strftime("%Y-%m-%dT00:00:00")

	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user=user)
	login = cad.login
	user_id = cad.id
	chave_cod = cad.cod_cliente
	revenda = cad.revenda

	cliente = Cadastro.objects.only('login')

	numero = request.GET.get('numero', '')
	operadora = request.GET.get('operadora', '')
	estado = request.GET.get('estado', '')
	cidade = request.GET.get('cidade', '')
	portado = request.GET.get('portado', '')
	tipo = request.GET.get('tipo', '')
	rn1 = request.GET.get('rn1', '')
	data = request.GET.get('calldate1', ontem)
	data2 = request.GET.get('calldate2', hoje)

	if revenda == 1:
		usuario = request.GET.get('cliente', login)
		cad = Cadastro.objects.get(login=usuario)
		user_id = cad.id
		results = Cdr.objects.only().filter(cliente_id=cad.id)
	else:
		results = Cdr.objects.only().filter(cliente_id=cad.id)

	n_numero = results.values_list('numero').distinct()
	n_operadora = results.values_list('operadora').distinct()
	n_cidade = results.values_list('cidade').distinct()
	n_estado = results.values_list('estado').distinct()
	n_portado = results.values_list('portado').distinct()
	n_tipo = results.values_list('tipo').distinct()
	n_rn1 = results.values_list('rn1').distinct()
	n_data = results.values_list('data').distinct()

	results_v = results.filter(numero__startswith=numero,operadora__contains=operadora,cidade__contains=cidade,
								estado__contains=estado,portado__contains=portado,tipo__contains=tipo,rn1__contains=rn1,
								data_hora__range=[data,data2]).order_by('-data_hora')

	soma = results_v.aggregate(Sum('valor'))['valor__sum']

	if request.method == 'GET':
		results = results_v
	else:
		results = results

	paginator = Paginator(results, 15)
	page = request.GET.get('page')

	try:
		contacts = paginator.page(page)
	
	except PageNotAnInteger:
		contacts = paginator.page(1)

	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	return render(request, 'cdr.html', locals())

@login_required
def operadoras(request):

	## Conexão ao banco MySQL
	try:
		c = connection.cursor()
		
		try:
			x = Cadastro.objects.get(user_id=request.user.id)
			id_cliente = x.id
			chave_cod = x.cod_cliente
			revenda = x.revenda
		
		except ObjectDoesNotExist:

			return redirect('/portabilidade/criar-user/')

		p = PlanoCliente.objects.get(cliente_id=id_cliente)
		plano = p.consultas
		tipo = p.tipo
		id_plano = p.plano
		expira = p.expira_em
		operadoras = Cdr.objects.values('operadora','tipo').order_by('operadora').annotate(Count('cidade')).filter(cliente=id_cliente)
		tipo_numero = Cdr.objects.values('tipo').annotate(Count('tipo')).filter(cliente=id_cliente)
		ultimos_numero = operadoras = Cdr.objects.values('numero','operadora','tipo','data_hora','valor').order_by('-id').filter(cliente=id_cliente)[:5][::1]

		try:

			consultas = p.consultas

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
						  COUNT( IF( tipo='RADIO', 1, NULL ) ) AS radio,
						  SUM(valor) AS valor
						FROM port_cdr WHERE cliente_id = %d
						GROUP BY operadora ORDER BY movel DESC""" % id_cliente
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

		paginator = Paginator(total, 6)
		page = request.GET.get('page')

		try:
			contacts = paginator.page(page)
		
		except PageNotAnInteger:
			contacts = paginator.page(1)

		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		portados = Cdr.objects.values('portado').annotate(cnt=Count('portado')).order_by('portado').filter(cliente_id=id_cliente)
		total_items = Cdr.objects.filter(cliente_id=id_cliente).count()
		total_items = float(total_items)

		items = [
	        {'portados': g['portado'], 'value': g['cnt'] * 100 / total_items} for g in portados
	    ]

		return render(request, 'operadoras.html', locals())
	
	except IndexError:
		return redirect('/portabilidade/meus-dados/')

@ratelimit(key='ip', rate='40/m', block=True)
def consulta(request,numero):

	hoje = datetime.datetime.now()
	segredo = request.GET['key']
	segredo = str(segredo)

	### Chama a função que checa o ID do usuário
	id_user = funcoes.pega_id_user(segredo)
	
	if id_user == None:
		rn1 = 'error - Chave não autoriada'
		response = HttpResponse(rn1, content_type='text/plain')
		return response
	else:
		id_user = id_user

	### Chama a função que checa o saldo do cliente
	saldo,tipo,diferenca = funcoes.checa_saldo(id_user)

	if diferenca >= 30:
		PlanoCliente.objects.filter(cliente_id=id_user).update(consultas=0,plano=1,nome_plano='Escolha um plano',tipo=1)

	if (saldo <= 0) and (tipo == 1):

		rn1 = 'error - Sem credito'
		response = HttpResponse(rn1, content_type='text/plain')
		return response
	else:

		tamanho = len(numero)
		
		key = request.GET['key']
		key = str(key)
		chave = funcoes.checa_chave(key)

		if key == chave:
			z = PlanoCliente.objects.get(cliente_id=id_user)
			retorno = z.retorno
			user_id = z.cliente
			ddd = z.ddd
			y = str(ddd)
			x = str(numero)

			if tamanho <= 9:

				numero = y + x
				csp = funcoes.numero_10(numero,user_id)
	
				if csp == None:
					rn1 = 'error - numero ou prefixo nao existe'
					response = HttpResponse(rn1, content_type='text/plain')
					return response	

				else:
					if retorno == '1':
						rn1 = csp
					else:
						rn1 = csp
						z = str(rn1)[3:]
						rn1 = '0' + z		
			
			if tamanho == 10:

				### Chama a função que checa retorna o CSP para números de 10 dígitos
				csp = funcoes.numero_10(numero,user_id)
				if numero == None:
					rn1 = 'error - numero ou prefixo nao existe'
					response = HttpResponse(rn1, content_type='text/plain')
					return response	
				else:
					if retorno == '1':
						rn1 = csp
					else:
						rn1 = csp
						z = str(rn1)[3:]
						rn1 = '0' + z

			if tamanho == 11:

				### Chama a função que checa retorna o CSP para números de 11 dígitos
				csp = funcoes.numero_11(numero,user_id)
				if csp == None:
					rn1 = 'error - numero ou prefixo nao existe'
					response = HttpResponse(rn1, content_type='text/plain')
					return response	

				else:
					if retorno == '1':
						rn1 = csp
					else:
						rn1 = csp
						z = str(rn1)[3:]
						rn1 = '0' + z

			### Chama a função que insere no CELERY, e o CELERY debita e insere no CDR
			insert_cdr.apply_async(kwargs={'request': chave, 'numero': numero},countdown=settings.TEMPO_ESPERA_CDR)	


			response = HttpResponse(rn1, content_type='text/plain')
			return response

		else:

			rn1 = 0
			response = HttpResponse(rn1, content_type='text/plain')
			return response

def retorno(request):

	retorno = request.GET['id_pagseguro']
	try:

		x = Retorno.objects.get(code=retorno)
		reference = x.reference
		z = Cadastro.objects.get(cod_cliente=reference)
		user_id = z.id
		atualiza_compra.apply_async(kwargs={'retorno': retorno},countdown=1)		

	
	except ObjectDoesNotExist:

		retorno = request.GET['id_pagseguro']
		atualiza_compra.apply_async(kwargs={'retorno': retorno},countdown=1)
	
	return redirect('/portabilidade/financeiro/')

def procura(request):

	x = Retorno.objects.values_list('code').filter(status=4)
	for v in x:
		code = v[0]

def gsm(request,key):

	hoje = datetime.datetime.now()
	numero = request.GET['numero']
	segredo = key
	segredo = str(segredo)

	### Chama a função que checa o ID do usuário
	id_user = funcoes.pega_id_user(segredo)
	
	if id_user == None:
		rn1 = 'error - Chave não autoriada'
		response = HttpResponse(rn1, content_type='text/plain')
		return response
	else:
		id_user = id_user

	### Chama a função que checa o saldo do cliente
	saldo,tipo,diferenca = funcoes.checa_saldo(id_user)

	if diferenca >= 30:
		PlanoCliente.objects.filter(cliente_id=id_user).update(consultas=0,plano=1,nome_plano='Escolha um plano',tipo=1)

	if (saldo <= 0) and (tipo == 1):

		rn1 = 'error - Sem credito'
		response = HttpResponse(rn1, content_type='text/plain')
		return response
	else:

		tamanho = len(numero)
		
		key = key
		key = str(key)
		chave = funcoes.checa_chave(key)

		if key == chave:

			if tamanho <= 9:
				rn1 = 'error - somente aceito 10 e 11 digitos'
				response = HttpResponse(rn1, content_type='text/plain')
				return response				
			
			if tamanho == 10:

				### Chama a função que checa retorna o CSP para números de 10 dígitos
				csp = funcoes.numero_10(numero)
				if numero == None:
					rn1 = 'error - numero ou prefixo nao existe'
					response = HttpResponse(rn1, content_type='text/plain')
					return response	
				else:
					rn1 = csp

			if tamanho == 11:

				### Chama a função que checa retorna o CSP para números de 11 dígitos
				csp = funcoes.numero_11(numero)
				if csp == None:
					rn1 = 'error - numero ou prefixo nao existe'
					response = HttpResponse(rn1, content_type='text/plain')
					return response	

				else:
					rn1 = csp

			### Chama a função que insere no CELERY, e o CELERY debita e insere no CDR
			insert_cdr.apply_async(kwargs={'request': chave, 'numero': numero},countdown=settings.TEMPO_ESPERA_CDR)	

			response = HttpResponse(rn1, content_type='text/plain')
			return response	

		else:

			rn1 = 0
			response = HttpResponse(rn1, content_type='text/plain')
			return response

