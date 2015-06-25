# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NaoPortados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operadora', models.CharField(max_length=64)),
                ('tipo', models.CharField(max_length=64)),
                ('prefixo', models.BigIntegerField()),
                ('rn1', models.IntegerField()),
            ],
            options={
                'db_table': 'nao_portados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Portados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.BigIntegerField()),
                ('rn1', models.IntegerField()),
                ('data_hora', models.DateTimeField()),
                ('op', models.IntegerField()),
            ],
            options={
                'db_table': 'portados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prefixo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ddd', models.IntegerField(null=True, blank=True)),
                ('prefixo', models.IntegerField(unique=True, null=True, blank=True)),
                ('inicial', models.IntegerField(null=True, blank=True)),
                ('final', models.IntegerField(null=True, blank=True)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('operadora', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=20)),
                ('rn1', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'prefixo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo', choices=[(b'Pessoa Fisica', b'Pessoa Fisica'), (b'Pessoa Juridica', b'Pessoa Juridica')])),
                ('first_name', models.CharField(max_length=100, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=200, verbose_name='SobreNome')),
                ('empresa', models.CharField(max_length=100, null=True, verbose_name='Nome fantasia', blank=True)),
                ('cpf', models.CharField(max_length=20, unique=True, null=True, verbose_name='CPF', blank=True)),
                ('cnpj', models.CharField(max_length=20, unique=True, null=True, verbose_name='CNPJ', blank=True)),
                ('ie', models.CharField(max_length=20, null=True, verbose_name='Insc. Estadual', blank=True)),
                ('telefoneF', models.CharField(max_length=20, null=True, verbose_name='Telefone Fixo', blank=True)),
                ('telefoneM', models.CharField(max_length=20, null=True, verbose_name='Telefone Movel', blank=True)),
                ('email', models.EmailField(max_length=254, unique=True, null=True, verbose_name=b'Email', blank=True)),
                ('email_contato', models.EmailField(max_length=254, null=True, verbose_name=b'Email contato', blank=True)),
                ('nome', models.CharField(max_length=100, null=True, verbose_name='Nome', blank=True)),
                ('endereco', models.CharField(max_length=100, null=True, verbose_name='Endere\xe7o', blank=True)),
                ('numero', models.CharField(max_length=100, null=True, verbose_name='N\xfamero', blank=True)),
                ('bairro', models.CharField(max_length=100, null=True, verbose_name='Bairro', blank=True)),
                ('complemento', models.CharField(max_length=100, null=True, verbose_name='Complemento', blank=True)),
                ('cidade', models.CharField(max_length=100, null=True, verbose_name='Cidade', blank=True)),
                ('estado', models.CharField(max_length=100, null=True, verbose_name='Estado', blank=True)),
                ('cep', models.CharField(default=b'00000-000', max_length=10, verbose_name='CEP')),
                ('cod_cliente', models.IntegerField(unique=True, verbose_name='Codigo do Cliente')),
                ('chave', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('consultas', models.IntegerField(default=0, verbose_name='Consultas')),
            ],
        ),
        migrations.CreateModel(
            name='Cdr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=30)),
                ('prefixo', models.IntegerField()),
                ('ddd', models.IntegerField()),
                ('rn1', models.IntegerField()),
                ('operadora', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=20)),
                ('portado', models.IntegerField(default=0)),
                ('data', models.DateField(auto_now=True)),
                ('hora', models.TimeField(auto_now=True)),
                ('data_hora', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(to='port.Cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plano', models.CharField(max_length=255, null=True, blank=True)),
                ('descricao', models.CharField(max_length=255, null=True, blank=True)),
                ('valor', models.DecimalField(default=0.0, null=True, max_digits=2, decimal_places=2, blank=True)),
                ('valor_consulta', models.FloatField(default=0.0, null=True, blank=True)),
                ('consultas_gratis', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanoCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consultas', models.IntegerField(default=0, null=True, blank=True)),
                ('consultas_gratis', models.IntegerField(default=0, null=True, blank=True)),
                ('cliente', models.OneToOneField(to='port.Cadastro')),
                ('plano', models.OneToOneField(to='port.Plano')),
            ],
        ),
        migrations.AddField(
            model_name='cadastro',
            name='plano',
            field=models.OneToOneField(default=1, to='port.Plano'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
