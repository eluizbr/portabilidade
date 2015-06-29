# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^operadoras/$', views.operadoras, name='operadoras'),
    url(r'^meus-dados/$', views.meus_dados, name='meus-dados'),
	url(r'^info/(?P<id>\d+)$', views.financeiro_info, name='info'),
	url(r'^comprar/$', views.comprar, name='comprar'),
    url(r'^financeiro/$', views.financeiro, name='financeiro'),
    url(r'^(?P<numero>\d+)$', views.consulta, name='consulta'),
    url(r'^retorno/$', views.retorno, name='retorno'),
    url(r'^retorno/pagseguro/', include('pagseguro.urls')),
)
