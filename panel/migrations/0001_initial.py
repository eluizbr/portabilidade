# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoRevenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='E-mail')),
                ('telefone_fixo', models.CharField(max_length=12, verbose_name='Telefone fixo')),
                ('telefone_celular', models.CharField(max_length=12, verbose_name='Telefone celular')),
            ],
        ),
        migrations.CreateModel(
            name='Revenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('endereco', models.CharField(help_text='Ex: Avenida Brasil, 950', max_length=200)),
                ('estado', models.CharField(max_length=2, verbose_name='Estado', choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amap\xc3\xa1'), (b'AM', b'Amazonas'), (b'BA', b'Bahia'), (b'CE', b'Ceara'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maranh\xc3\xa3o'), (b'MT', b'Mato Grosso'), (b'MS', b'Mato Grosso do Sul'), (b'MG', b'Minas Gerais'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PR', b'Paran\xc3\xa1'), (b'PE', b'Pernambuco'), (b'PI', b'Piau\xc3\xad'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RS', b'Rio Grande do Sul'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'SC', b'Santa Catarina'), (b'SP', b'S\xc3\xa3o Paulo'), (b'SE', b'Sergipe'), (b'TO', b'Tocantins')])),
                ('nome_contato', models.CharField(max_length=80, verbose_name='Nome do contato')),
            ],
        ),
        migrations.AddField(
            model_name='contatorevenda',
            name='revenda',
            field=models.ForeignKey(to='panel.Revenda'),
        ),
    ]
