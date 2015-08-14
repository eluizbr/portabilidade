# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0027_auto_20150814_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='login',
            field=models.CharField(default=0, unique=True, max_length=30, verbose_name='Login de acesso'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='senha',
            field=models.CharField(default=0, max_length=100, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 11, 10, 55, 710779)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 11, 10, 55, 710779)),
        ),
    ]
