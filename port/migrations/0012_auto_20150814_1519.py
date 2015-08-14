# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0011_auto_20150814_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='cod_cliente',
            field=models.ManyToManyField(related_name='cliente', to='port.Cadastro', blank=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 15, 19, 45, 229666)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 15, 19, 45, 229666)),
        ),
    ]
