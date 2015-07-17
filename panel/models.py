# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from dry.models import DateModel
from dry.choices import ESTADOS_CHOICE


class Revenda(DateModel):
    razao_social = models.CharField(max_length=100,
                                    verbose_name=_('Razão Social'))
    nome_fantasia = models.CharField(max_length=100,
                                     verbose_name=_('Nome fantasia'))
    cnpj = models.CharField(max_length=14, verbose_name=_('CNPJ'))
    inscricao_estadual = models.CharField(max_length=30,
                                          verbose_name=_("Inscrição estadual"),
                                          blank=True, null=True)
    endereco = models.CharField(max_length=200,
                                verbose_name=_('Endereço'),
                                help_text=_('Ex: Avenida Brasil, 950'))
    # @TODO --> Must define a choice
    estado = models.CharField(max_length=2, verbose_name=_("Estado"),
                              choices=ESTADOS_CHOICE)
    nome_contato = models.CharField(max_length=80,
                                    verbose_name=_("Nome do contato"))

    def __unicode__(self):
        return self.nome_fantasia


class ContatoRevenda(models.Model):
    revenda = models.ForeignKey("Revenda")
    email = models.EmailField(verbose_name=_("E-mail"), unique=True)
    telefone_fixo = models.CharField(max_length=12,
                                     verbose_name=_("Telefone fixo"))
    telefone_celular = models.CharField(max_length=12,
                                        verbose_name=_("Telefone celular"))

    def __unicode__(self):
        return self.email
