# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0013_auto_20150814_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='retorno',
            name='cliente',
            field=models.ForeignKey(default=1, blank=True, to='port.Cadastro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='cod_revenda',
            field=models.CharField(default=b'0', max_length=100, verbose_name='Codigo da Revenda'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 17, 8, 55, 858097)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 17, 8, 55, 858097)),
        ),
    ]
