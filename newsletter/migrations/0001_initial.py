# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='envio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(default=b'(00)0000-0000', max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('empresa', models.CharField(max_length=255)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('enviado', models.IntegerField(default=0)),
                ('tipo', models.CharField(default=b'Parceiro', max_length=25, choices=[('Parceiro', b'Parceiro'), ('Cliente', b'Cliente')])),
            ],
        ),
    ]
