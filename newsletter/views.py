# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from models import envio,PostOfficeEmailtemplate
from forms import EnvioForm
from post_office import mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index_envio(request):

	# empresas = envio.objects.all()
	# return render(request,'envio.html', locals())
	return redirect('cadastro')

def cadastro(request):

	
	if request.method == 'POST':
		form = EnvioForm(request.POST)
			
		if form.is_valid():
			form.save()
			return redirect('/envio/cadastro/')

	else:

		form = EnvioForm()

	empresas = envio.objects.all()
	paginator = Paginator(empresas, 15)
	page = request.GET.get('page')

	try:
		contacts = paginator.page(page)
	
	except PageNotAnInteger:
		contacts = paginator.page(1)

	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)


	return render(request,'cadastro.html', locals())

def enviar(request):

	pega = envio.objects.values('email','nome','enviado','template_id')

	for e in pega:

		email = e['email']
		nome = e['nome']
		enviado = e['enviado']
		template = e['template_id']
		x = PostOfficeEmailtemplate.objects.get(id=template)
		template = x.name
		print nome,email,enviado,template

		if enviado == 0:
			mail.send(
			    [email],
			    sender=settings.DEFAULT_FROM_EMAIL,
			    template=template,
			    context={'nome': nome},
			)

		envio.objects.filter(email=email).update(enviado=1)

	return redirect('/envio/cadastro/')



