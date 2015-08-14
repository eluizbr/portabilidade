# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0010_auto_20150814_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigo_revenda',
            name='revenda',
            field=models.CharField(unique=True, max_length=100, verbose_name='Codigo da Revenda'),
        ),
    ]
