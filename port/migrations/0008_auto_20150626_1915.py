# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0007_auto_20150626_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='retorno',
            name='id_plano',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='retorno',
            name='status',
            field=models.CharField(default=1, max_length=200, choices=[(b'1', b'Aguardando pagamento'), (b'2', b'Em an\xc3\xa1lise'), (b'3', b'Pago'), (b'4', b'Dispon\xc3\xadvel'), (b'5', b'Em disputa'), (b'6', b'Devolvido'), (b'7', b'Cancelado'), (b'8', b'Valor devolvido'), (b'9', b'Em contesta\xc3\xa7\xc3\xa3o')]),
        ),
    ]
