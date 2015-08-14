# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo', choices=[(b'Pessoa Fisica', b'Pessoa Fisica'), (b'Pessoa Juridica', b'Pessoa Juridica')])),
                ('first_name', models.CharField(max_length=100, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=200, verbose_name='SobreNome')),
                ('empresa', models.CharField(max_length=100, null=True, verbose_name='Nome fantasia', blank=True)),
                ('cpf', models.CharField(unique=True, max_length=20, verbose_name='CPF')),
                ('cnpj', models.CharField(max_length=20, null=True, verbose_name='CNPJ', blank=True)),
                ('ie', models.CharField(max_length=20, null=True, verbose_name='Insc. Estadual', blank=True)),
                ('telefoneF', models.CharField(max_length=20, null=True, verbose_name='Telefone Fixo', blank=True)),
                ('telefoneM', models.CharField(max_length=20, null=True, verbose_name='Telefone Movel', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'Email')),
                ('email_contato', models.EmailField(max_length=254, null=True, verbose_name=b'Email contato', blank=True)),
                ('nome', models.CharField(max_length=100, null=True, verbose_name='Nome', blank=True)),
                ('endereco', models.CharField(max_length=100, null=True, verbose_name='Endere\xe7o', blank=True)),
                ('numero', models.CharField(max_length=100, null=True, verbose_name='N\xfamero', blank=True)),
                ('bairro', models.CharField(max_length=100, null=True, verbose_name='Bairro', blank=True)),
                ('complemento', models.CharField(max_length=100, null=True, verbose_name='Complemento', blank=True)),
                ('cidade', models.CharField(max_length=100, null=True, verbose_name='Cidade', blank=True)),
                ('estado', models.CharField(max_length=100, null=True, verbose_name='Estado', blank=True)),
                ('cep', models.CharField(default=b'00000-000', max_length=10, verbose_name='CEP')),
                ('cod_revenda', models.IntegerField(unique=True, verbose_name='Codigo da Revenda')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
