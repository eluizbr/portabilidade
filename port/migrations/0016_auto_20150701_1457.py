# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0015_plano_taxas'),
    ]

    operations = [
        migrations.AddField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.date(2015, 7, 1)),
        ),
        migrations.AddField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.date(2015, 7, 31)),
        ),
    ]
