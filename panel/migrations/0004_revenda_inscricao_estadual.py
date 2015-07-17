# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20150717_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenda',
            name='inscricao_estadual',
            field=models.CharField(max_length=30, null=True, verbose_name='Inscri\xe7\xe3o estadual', blank=True),
        ),
    ]
