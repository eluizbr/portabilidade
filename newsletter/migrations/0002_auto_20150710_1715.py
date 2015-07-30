# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostOfficeEmailtemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('html_content', models.TextField()),
                ('created', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'post_office_emailtemplate',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='envio',
            name='template',
            field=models.ForeignKey(default=11, to='newsletter.PostOfficeEmailtemplate'),
        ),
    ]
