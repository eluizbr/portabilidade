# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0003_remove_cadastro_consultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='retorno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('lastEventDate', models.DateTimeField()),
                ('code', models.CharField(max_length=200)),
                ('reference', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
                ('paymentMethod', models.IntegerField()),
                ('paymentMethodCode', models.IntegerField()),
                ('grossAmount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('discountAmount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('netAmount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('extraAmount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
        ),
    ]
