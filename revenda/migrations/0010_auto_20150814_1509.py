# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0009_auto_20150814_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codigo_revenda',
            old_name='cliente_id',
            new_name='cliente',
        ),
    ]
