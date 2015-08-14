# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0023_auto_20150811_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='cod_cliente',
            field=models.ManyToManyField(related_name='cliente', to='port.Cadastro'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 9, 33, 28, 263746)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 9, 33, 28, 263746)),
        ),
    ]
