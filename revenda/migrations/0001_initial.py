# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0018_auto_20150815_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo_revenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revenda', models.CharField(default=0, unique=True, max_length=100, verbose_name='Codigo da Revenda')),
                ('cliente', models.ForeignKey(to='port.Cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Comissao_revenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=100, verbose_name='Login do Cliente')),
                ('Nome', models.CharField(max_length=100, verbose_name='Nome do Cliente')),
                ('revenda', models.CharField(max_length=100, verbose_name='Codigo da Revenda')),
                ('data_compra', models.DateTimeField()),
                ('comissao', models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('mes', models.IntegerField(default=8, null=True, blank=True)),
                ('ano', models.IntegerField(default=2015, null=True, blank=True)),
                ('retorno', models.ForeignKey(to='port.Retorno')),
            ],
        ),
    ]
