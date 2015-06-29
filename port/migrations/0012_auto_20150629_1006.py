# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0011_auto_20150629_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retorno',
            old_name='nome',
            new_name='name',
        ),
    ]
