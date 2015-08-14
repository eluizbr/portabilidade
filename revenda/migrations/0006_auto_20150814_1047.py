# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0005_auto_20150814_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenda',
            name='login',
            field=models.CharField(unique=True, max_length=30, verbose_name='Login de acesso'),
        ),
    ]
