# -*- coding: UTF-8 -*-
from django.http import Http404
from django.conf.urls import patterns, include, url
from rest_framework import routers
from port import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^pabx/$', views.asterisk, name='pabx'),
    url(r'^padrao/$', views.padrao, name='padrao'),
    url(r'^csp-retorno/$', views.csp_retorno, name='csp-retorno'),
    url(r'^csp-retorno-del/(?P<deletar>\d+)$', views.csp_retorno_del, name='csp-retorno-del'),
    url(r'^csp/$', views.csp, name='csp'),
    url(r'^cdr/$', views.cdr, name='cdr'),
    url(r'^operadoras/$', views.operadoras, name='operadoras'),
    url(r'^criar-user/$', views.criar_user, name='criar-user'),
    url(r'^meus-dados/$', views.meus_dados, name='meus-dados'),
	url(r'^info/(?P<id>\d+)$', views.financeiro_info, name='info'),
	# url(r'^comprar/$', views.comprar, name='comprar'),
    url(r'^financeiro/$', views.financeiro, name='financeiro'),
    url(r'^(?P<numero>\d+)$', views.consulta, name='consulta'),
    url(r'^consulta/(?P<key>\d+)$', views.gsm, name='gsm'),
    url(r'^retorno/$', views.retorno, name='retorno'),
    url(r'^retorno/pagseguro/', include('pagseguro.urls')),
    
)
