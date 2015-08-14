# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0021_auto_20150806_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano',
            name='cliente',
            field=models.ManyToManyField(default=0, related_name='cliente', to='port.Cadastro'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 9, 29, 0, 25283)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 9, 29, 0, 25283)),
        ),
    ]
