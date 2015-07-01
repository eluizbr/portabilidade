# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0016_auto_20150701_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='planocliente',
            name='tipo',
            field=models.CharField(default=1, max_length=200, choices=[(b'0', b'Ilimitado'), (b'1', b'normal')]),
        ),
    ]
