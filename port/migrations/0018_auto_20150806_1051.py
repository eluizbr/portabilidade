# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0017_auto_20150806_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cspretorno',
            name='operadora',
        ),
        migrations.RemoveField(
            model_name='cspretorno',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 6, 10, 51, 40, 185126)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 10, 51, 40, 185126)),
        ),
    ]
