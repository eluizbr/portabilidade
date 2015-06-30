# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0014_auto_20150629_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano',
            name='taxas',
            field=models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
