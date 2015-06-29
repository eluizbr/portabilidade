# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0010_retorno_consultas'),
    ]

    operations = [
        migrations.AddField(
            model_name='retorno',
            name='email',
            field=models.EmailField(default=b'email@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='retorno',
            name='nome',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='retorno',
            name='phone',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
