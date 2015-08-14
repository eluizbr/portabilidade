# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0002_auto_20150814_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenda',
            name='login',
            field=models.CharField(default=0, max_length=30, verbose_name='Login'),
        ),
        migrations.AddField(
            model_name='revenda',
            name='senha',
            field=models.CharField(default=0, max_length=100, verbose_name='Senha'),
        ),
    ]
