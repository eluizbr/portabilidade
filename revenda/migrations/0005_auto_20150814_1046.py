# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0004_auto_20150814_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenda',
            name='login',
            field=models.CharField(default=0, unique=True, max_length=30, verbose_name='Login de acesso'),
        ),
        migrations.AlterField(
            model_name='revenda',
            name='senha',
            field=models.CharField(max_length=100, verbose_name='Senha'),
        ),
    ]
