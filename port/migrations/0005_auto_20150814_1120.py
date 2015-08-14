# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0004_auto_20150814_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='revenda',
            field=models.IntegerField(default=0, verbose_name='Revenda'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 11, 20, 2, 48796)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 11, 20, 2, 48796)),
        ),
    ]
