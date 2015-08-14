# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0010_auto_20150814_1508'),
        ('revenda', '0008_auto_20150814_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo_revenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revenda', models.CharField(default=0, unique=True, max_length=100, verbose_name='Codigo da Revenda')),
                ('cliente_id', models.ForeignKey(to='port.Cadastro')),
            ],
        ),
        migrations.DeleteModel(
            name='Clientes_revenda',
        ),
    ]
