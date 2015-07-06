# -*- coding: UTF-8 -*-
from django.http import Http404
from django.conf.urls import patterns, include, url
from newsletter import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index_envio, name='index_envio'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^enviar/$', views.enviar, name='enviar'),

)