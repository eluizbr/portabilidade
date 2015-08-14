# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0007_auto_20150814_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='especial',
            field=models.CharField(default=0, max_length=200, verbose_name='Plano', choices=[(b'0', b'Liberado'), (b'1', b'Restrito')]),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='cliente',
            field=models.ForeignKey(to='port.Cadastro'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 14, 56, 0, 460425)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 14, 56, 0, 460425)),
        ),
    ]
