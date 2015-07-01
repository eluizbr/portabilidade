# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0017_planocliente_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano',
            name='tipo',
            field=models.CharField(default=1, max_length=200, choices=[(b'0', b'Ilimitado'), (b'1', b'normal')]),
        ),
    ]
