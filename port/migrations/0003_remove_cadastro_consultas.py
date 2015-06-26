# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_auto_20150626_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='consultas',
        ),
    ]
