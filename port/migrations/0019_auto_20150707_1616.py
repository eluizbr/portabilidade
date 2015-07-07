# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0018_plano_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SipBuddies',
            fields=[
                ('uniqueid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=250)),
                ('accountcode', models.CharField(max_length=30, null=True, blank=True)),
                ('amaflags', models.CharField(max_length=1, null=True, blank=True)),
                ('callgroup', models.CharField(max_length=30, null=True, blank=True)),
                ('callerid', models.CharField(max_length=50, null=True, blank=True)),
                ('canreinvite', models.CharField(max_length=3, null=True, blank=True)),
                ('context', models.CharField(max_length=250, null=True, blank=True)),
                ('defaultip', models.CharField(max_length=15, null=True, blank=True)),
                ('dtmfmode', models.CharField(max_length=7, null=True, blank=True)),
                ('fromuser', models.CharField(max_length=50, null=True, blank=True)),
                ('fromdomain', models.CharField(max_length=31, null=True, blank=True)),
                ('host', models.CharField(max_length=31)),
                ('incominglimit', models.CharField(max_length=2, null=True, blank=True)),
                ('outgoinglimit', models.CharField(max_length=2, null=True, blank=True)),
                ('insecure', models.CharField(max_length=4, null=True, blank=True)),
                ('language', models.CharField(max_length=2, null=True, blank=True)),
                ('mailbox', models.CharField(max_length=50, null=True, blank=True)),
                ('md5secret', models.CharField(max_length=32, null=True, blank=True)),
                ('nat', models.CharField(max_length=5, null=True, blank=True)),
                ('permit', models.CharField(max_length=95, null=True, blank=True)),
                ('deny', models.CharField(max_length=95, null=True, blank=True)),
                ('pickupgroup', models.CharField(max_length=30, null=True, blank=True)),
                ('port', models.CharField(max_length=5)),
                ('qualify', models.CharField(max_length=4, null=True, blank=True)),
                ('restrictcid', models.CharField(max_length=3, null=True, blank=True)),
                ('rtptimeout', models.CharField(max_length=3, null=True, blank=True)),
                ('rtpholdtimeout', models.CharField(max_length=3, null=True, blank=True)),
                ('secret', models.CharField(max_length=30, null=True, blank=True)),
                ('type', models.CharField(max_length=6)),
                ('username', models.CharField(max_length=30)),
                ('allow', models.CharField(max_length=100, null=True, blank=True)),
                ('disallow', models.CharField(max_length=100, null=True, blank=True)),
                ('regseconds', models.IntegerField()),
                ('ipaddr', models.CharField(max_length=15)),
                ('cliente', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sip_buddies',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='cpf',
            field=models.CharField(default=b'00000-000', unique=True, max_length=20, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='email',
            field=models.EmailField(default=b'email@emai.com', unique=True, max_length=254, verbose_name=b'Email'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 7, 16, 16, 41, 823366)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 6, 16, 16, 41, 823366)),
        ),
    ]
