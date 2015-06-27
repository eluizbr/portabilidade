# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0009_auto_20150626_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='retorno',
            name='consultas',
            field=models.IntegerField(default=0),
        ),
    ]
