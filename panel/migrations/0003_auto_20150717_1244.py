# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_auto_20150717_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenda',
            name='endereco',
            field=models.CharField(help_text='Ex: Avenida Brasil, 950', max_length=200, verbose_name='Endere\xe7o'),
        ),
        migrations.AlterField(
            model_name='revenda',
            name='razao_social',
            field=models.CharField(max_length=100, verbose_name='Raz\xe3o Social'),
        ),
    ]
