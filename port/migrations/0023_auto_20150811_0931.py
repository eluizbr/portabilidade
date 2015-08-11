# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0022_auto_20150811_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plano',
            old_name='cliente',
            new_name='cod_cliente',
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 9, 31, 2, 698798)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 9, 31, 2, 698798)),
        ),
    ]
