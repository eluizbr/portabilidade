# -*- coding: UTF-8 -*-
from django.http import Http404
from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^asterisk/$', views.asterisk, name='asterisk'),
    url(r'^csp/$', views.csp, name='csp'),
    url(r'^operadoras/$', views.operadoras, name='operadoras'),
    url(r'^criar-user/$', views.criar_user, name='criar-user'),
    url(r'^meus-dados/$', views.meus_dados, name='meus-dados'),
	url(r'^info/(?P<id>\d+)$', views.financeiro_info, name='info'),
	# url(r'^comprar/$', views.comprar, name='comprar'),
    url(r'^financeiro/$', views.financeiro, name='financeiro'),
    url(r'^(?P<numero>\d+)$', views.consulta, name='consulta'),
    url(r'^retorno/$', views.retorno, name='retorno'),
    url(r'^retorno/pagseguro/', include('pagseguro.urls')),

)
