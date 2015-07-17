# -*- coding: UTF-8 -*-
from django.http import Http404
from django.conf.urls import patterns, include, url
from rest_framework import routers

from .views import CreateRevenda


urlpatterns = patterns('',
    url(r'^$', CreateRevenda.as_view(), name='create-revenda'),
    # url(r'^create-revenda/', CreteRevenda.as_view(), name='create-revenda'),
)
