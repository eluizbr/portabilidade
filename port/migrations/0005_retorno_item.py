# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0004_retorno'),
    ]

    operations = [
        migrations.AddField(
            model_name='retorno',
            name='item',
            field=models.CharField(default=b'item', max_length=200),
        ),
    ]
