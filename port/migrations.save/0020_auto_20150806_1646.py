# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0019_auto_20150806_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdr',
            name='retorno',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 6, 16, 46, 29, 727623)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 16, 46, 29, 727623)),
        ),
    ]
