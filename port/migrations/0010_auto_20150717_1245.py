# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20150717_1244'),
        ('port', '0009_auto_20150717_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='revenda',
            field=models.ForeignKey(default=None, blank=True, to='panel.Revenda', null=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 17, 12, 45, 31, 773484)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 16, 12, 45, 31, 773484)),
        ),
    ]
