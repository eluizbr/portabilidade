# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_envio_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='empresa',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='envio',
            name='enviado',
            field=models.IntegerField(default=0),
        ),
    ]
