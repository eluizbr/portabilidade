# -*- coding: UTF-8 -*-
from django.http import Http404
from django.conf.urls import patterns, include, url
from revenda import views


urlpatterns = patterns('',
    # Examples:
    url(r'^revenda-dados/$', views.revenda_dados, name='revenda-dados'),
    url(r'^criar-revenda/$', views.criar_revenda, name='criar-revenda'),
    url(r'^meus-clientes/$', views.meus_clientes, name='meus-clientes'),
    url(r'^info/(?P<id>\d+)$', views.pg_info, name='info'),
    url(r'^edit-cliente/(?P<id>\d+)$', views.editar_cliente, name='edit-cliente'),       
)
