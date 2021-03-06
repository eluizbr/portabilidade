# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from post_office import mail
from models import Codigo_revenda, Comissao_revenda
from port.models import Cadastro, PlanoCliente, SipBuddies, Retorno
from forms import RevendaForm
import uuid
import datetime
import random
import decimal
from datetime import timedelta,date,datetime
from django.db import connection

@login_required
def criar_revenda(request):

	data = datetime.now()
	mes = data + timedelta(days=30)
	user = User.objects.get(pk=request.user.id)
	revenda = Cadastro.objects.get(user_id=request.user.id)
	cod_revenda = revenda.cod_cliente

	cad = Cadastro.objects.get(user=request.user.id)
	cod_cliente = cad.id
	chave_cod = cad.cod_cliente
	revenda = cad.revenda
	x = Codigo_revenda.objects.get(cliente_id=cod_cliente)
	cod_revenda = x.revenda

	if request.method == 'POST':
		form = RevendaForm(request.POST)

		if form.is_valid():
			
			senha = str(uuid.uuid4().get_hex()[0:10])
			login = request.POST.get('login', '')
			email = request.POST.get('email', '')
			new_user = User.objects.create_user(username=login,email=email, password=senha)
			obj = form.save(commit=False)
			#obj.email = user.email
			obj.user = user
			obj.senha = senha
			obj.user_id = new_user.id
			obj.cod_cliente = int(random.randint(10000000, 99000000))
			obj.cod_revenda = cod_revenda
			obj.save()

			try:
				### Se o plano não exite, então cria...
				cad = Cadastro.objects.get(user=new_user.id)
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
				sip = SipBuddies(name=codigo_cliente,username=codigo_cliente,port=5060,secret=secret,regseconds=0,cliente=codigo_cliente)
				sip.save()	

				mail.send(
				    'eluizbr@gmail.com', # List of email addresses also accepted
				    sender=settings.DEFAULT_FROM_EMAIL,
				    template='usuario_novo',
				    context={'name': name,'phone':phone}
				)

			return redirect('/revenda/meus-clientes/')
	else:
		form = RevendaForm()

	return render(request, 'criar_revenda.html', locals())	

@login_required
def revenda_dados(request):

	user = User.objects.get(pk=request.user.id)

	try:
		cad = Cadastro.objects.get(user=user)
		user_id = cad.id
		codigo_cliente = cad.cod_cliente
		name = cad.first_name
		chave_cod = cad.cod_cliente

	except Cadastro.DoesNotExist:
		return redirect('/revenda/meus-clientes/')
	
	if request.method == 'POST':
		form = RevendaForm(request.POST or None, instance=cad)
		
		try:
			p = Cadastro.objects.get(user_id=request.user.id)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.save()
			else:
				form = RevendaForm(instance=cad)

		except Cadastro.DoesNotExist:
			
			if form.is_valid():
				obj = form.save(commit=False)
				obj.user = user
				obj.cod_cliente = str(uuid.uuid4().get_hex().upper()[0:10])
				obj.save()
	else:

		form = RevendaForm(instance=cad)

	return render(request, 'revenda_dados.html', locals())

@login_required
def pg_info(request,id):

    pg_info = Retorno.objects.all().filter(cliente_id=id)
    return render(request,'pg_info.html', locals())

@login_required
def editar_cliente(request,id):

	user = User.objects.get(pk=request.user.id)

	cad = Cadastro.objects.get(id=id)
	user_id = cad.id
	codigo_cliente = cad.cod_cliente
	name = cad.first_name
	chave_cod = cad.cod_cliente

	if request.method == 'POST':
		form = RevendaForm(request.POST or None, instance=cad)

		p = Cadastro.objects.get(user_id=request.user.id)
		if form.is_valid():

			obj = form.save(commit=False)
			obj.save()
		else:

			form = RevendaForm(instance=cad)
			obj = form.save(commit=False)
			obj.save()
			return redirect('/revenda/meus-clientes/')

	else:

		form = RevendaForm(instance=cad)
    
    	return render(request,'edit_cliente.html', locals())

@login_required
def meus_clientes(request):
	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user_id=user)
	cliente_id = cad.id
	chave_cod = cad.cod_cliente
	revenda = cad.revenda
	x = Codigo_revenda.objects.get(cliente_id=cliente_id)
	cod_revenda = x.revenda

	# Pega todos os clientes da revenda
	clientes = Cadastro.objects.all().filter(cod_revenda=cod_revenda)

	return render(request, 'meus_clientes.html', locals())

@login_required
def comissao(request):

	today = datetime.today()
	mes = today.month
	ano = today.year

	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user_id=user)
	revenda = cad.revenda
	cliente_id = cad.id
	chave_cod = cad.cod_cliente
	x = Codigo_revenda.objects.get(cliente_id=cliente_id)
	cod_revenda = x.revenda
	# Pega todos os clientes da revenda
	comissao = Comissao_revenda.objects.all().filter(revenda=cod_revenda,mes=mes,ano=ano)
	soma = comissao.aggregate(Sum('comissao'))['comissao__sum']

	c = connection.cursor()
	retorno = 'SELECT data_compra,SUM(comissao) AS comissao FROM revenda_comissao_revenda GROUP BY mes ORDER BY mes DESC'
	retorno = c.execute(retorno)
	retorno = c.fetchall()
	
	return render(request, 'comissao.html', locals())

@login_required
def pabx_info(request,id):

	user = User.objects.get(pk=request.user.id)
	cad = Cadastro.objects.get(user=id)
	login = cad.login
	chave = cad.chave
	chave_cod = cad.cod_cliente
	cod_cliente = cad.cod_cliente
	revenda = cad.revenda

	asterisk = SipBuddies.objects.get(cliente=cod_cliente)
	ast_user = asterisk.name
	ast_pass = asterisk.secret

	return render(request, 'pabx_info.html', locals())
