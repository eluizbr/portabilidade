# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0014_auto_20150728_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operadora', models.CharField(max_length=255, null=True, blank=True)),
                ('rn1', models.IntegerField(null=True, blank=True)),
                ('tipo', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'csp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CspRetorno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.IntegerField(null=True, blank=True)),
                ('csp', models.IntegerField(null=True, blank=True)),
                ('retorno', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 6, 9, 54, 58, 531369)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='ddd',
            field=models.IntegerField(default=31, null=True, verbose_name='DDD', blank=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 9, 54, 58, 531369)),
        ),
    ]
