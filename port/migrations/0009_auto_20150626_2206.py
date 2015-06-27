# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0008_auto_20150626_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='retorno',
            name='controle',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='retorno',
            name='id_plano',
            field=models.IntegerField(),
        ),
    ]
