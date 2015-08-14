# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0006_auto_20150814_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenda',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Sobrenome'),
        ),
    ]
