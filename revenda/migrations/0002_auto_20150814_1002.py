# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenda',
            name='cod_revenda',
            field=models.CharField(unique=True, max_length=100, verbose_name='Codigo da Revenda'),
        ),
    ]
