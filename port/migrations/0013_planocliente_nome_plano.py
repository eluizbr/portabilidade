# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0012_auto_20150629_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='planocliente',
            name='nome_plano',
            field=models.CharField(default=b'Ilimitado', max_length=255, verbose_name='Nome do Plano'),
        ),
    ]
