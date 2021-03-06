"""portabilidade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views



urlpatterns = [
    
    url(r'^api/$', views.ConsultaApi.as_view()),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^conta/', include('registration.backends.default.urls')),
    url(r'^portabilidade/', include('port.urls')),
    url(r'^revenda/', include('revenda.urls')),
    url(r'^envio/', include('newsletter.urls')),
    url(r'^$', RedirectView.as_view(pattern_name='operadoras')),
    url(r'^retorno/pagseguro/', include('pagseguro.urls')),


]

urlpatterns = format_suffix_patterns(urlpatterns)
