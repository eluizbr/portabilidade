# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0007_auto_20150814_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes_revenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revenda', models.IntegerField(verbose_name='Revenda')),
                ('cliente', models.IntegerField(verbose_name='Cliente ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='revenda',
            name='user',
        ),
        migrations.DeleteModel(
            name='Revenda',
        ),
    ]
