# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0020_auto_20150806_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cspretorno',
            name='csp',
            field=models.IntegerField(unique=True, null=True, verbose_name='CSP de origem', blank=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 6, 20, 27, 31, 890483)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 20, 27, 31, 890483)),
        ),
    ]
