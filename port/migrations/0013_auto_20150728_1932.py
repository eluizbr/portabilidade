# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0012_auto_20150728_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='planocliente',
            name='aviso_saldo',
            field=models.IntegerField(default=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 19, 32, 25, 816223)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 19, 32, 25, 816223)),
        ),
    ]
