# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comissao_revenda',
            old_name='Nome',
            new_name='nome',
        ),
    ]
