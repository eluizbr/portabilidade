# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0013_planocliente_nome_plano'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdr',
            name='valor',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='nome_plano',
            field=models.CharField(max_length=255, verbose_name='Nome do Plano'),
        ),
    ]
