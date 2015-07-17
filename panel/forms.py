# coding: utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms.models import inlineformset_factory

from dry.choices import ESTADOS_CHOICE
from .models import Revenda, ContatoRevenda


class CadastroRevendaForm(forms.ModelForm):
    razao_social = forms.CharField(label=_("Razão Social"))
    nome_fantasia = forms.CharField(label=_('Nome fantasia'))
    cnpj = forms.CharField(label=_('CNPJ'))
    inscricao_estadual = forms.CharField(label=_('Inscrição estadual'),
                                         required=False)
    endereco = forms.CharField(max_length=200,
                                label=_('Endereço'),
                                help_text=_('Ex: Avenida Brasil, 950'))
    estado = forms.ChoiceField(label=_("Estado"),
                              choices=ESTADOS_CHOICE, required=False)
    nome_contato = forms.CharField(label=_("Nome do contato"))

    class Meta:
        model = Revenda
        fields = [
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'inscricao_estadual',
            'endereco',
            'estado',
            'nome_contato'
        ]


ContatoRevendaFormSet = inlineformset_factory(Revenda, ContatoRevenda,
                                              extra=1,
                                              fields=('email',
                                                      'telefone_fixo',
                                                      'telefone_celular'))
