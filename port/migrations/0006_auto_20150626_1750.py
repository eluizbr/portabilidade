# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0005_retorno_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planocliente',
            name='cliente',
            field=models.IntegerField(default=1, unique=True, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='retorno',
            name='item',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='retorno',
            name='paymentMethod',
            field=models.CharField(default=1, max_length=200, choices=[(b'1', b'Cart\xc3\xa3o de cr\xc3\xa9dito'), (b'2', b'Boleto'), (b'3', b'D\xc3\xa9bito online (TEF)'), (b'4', b'Saldo PagSeguro'), (b'5', b'Oi Paggo'), (b'7', b'Dep\xc3\xb3sito em conta')]),
        ),
        migrations.AlterField(
            model_name='retorno',
            name='paymentMethodCode',
            field=models.CharField(default=101, max_length=200, choices=[(b'101', b'Cart\xc3\xa3o de cr\xc3\xa9dito Visa'), (b'102', b'Cart\xc3\xa3o de cr\xc3\xa9dito MasterCard'), (b'103', b'Cart\xc3\xa3o de cr\xc3\xa9dito American Express'), (b'104', b'Cart\xc3\xa3o de cr\xc3\xa9dito Diners'), (b'105', b'Cart\xc3\xa3o de cr\xc3\xa9dito Hipercard'), (b'106', b'Cart\xc3\xa3o de cr\xc3\xa9dito Aura'), (b'107', b'Cart\xc3\xa3o de cr\xc3\xa9dito Elo'), (b'108', b'Cart\xc3\xa3o de cr\xc3\xa9dito PLENOCard'), (b'109', b'Cart\xc3\xa3o de cr\xc3\xa9dito PersonalCard'), (b'110', b'Cart\xc3\xa3o de cr\xc3\xa9dito JCB'), (b'111', b'Cart\xc3\xa3o de cr\xc3\xa9dito Discover'), (b'112', b'Cart\xc3\xa3o de cr\xc3\xa9dito BrasilCard'), (b'113', b'Cart\xc3\xa3o de cr\xc3\xa9dito FORTBRASIL'), (b'114', b'Cart\xc3\xa3o de cr\xc3\xa9dito CARDBAN'), (b'115', b'Cart\xc3\xa3o de cr\xc3\xa9dito VALECARD'), (b'116', b'Cart\xc3\xa3o de cr\xc3\xa9dito Cabal'), (b'117', b'Cart\xc3\xa3o de cr\xc3\xa9dito Mais!'), (b'118', b'Cart\xc3\xa3o de cr\xc3\xa9dito Avista'), (b'119', b'Cart\xc3\xa3o de cr\xc3\xa9dito GRANDCARD'), (b'120', b'Cart\xc3\xa3o de cr\xc3\xa9dito Sorocred'), (b'201', b'Boleto Bradesco'), (b'202', b'Boleto Santander'), (b'301', b'D\xc3\xa9bito online Bradesco'), (b'302', b'D\xc3\xa9bito online Ita\xc3\xba'), (b'303', b'D\xc3\xa9bito online Unibanco'), (b'304', b'D\xc3\xa9bito online Banco do Brasil'), (b'305', b'D\xc3\xa9bito online Banco Real'), (b'306', b'D\xc3\xa9bito online Banrisul'), (b'307', b'D\xc3\xa9bito online HSBC'), (b'401', b'Saldo PagSeguro'), (b'501', b'Oi Paggo'), (b'701', b'Dep\xc3\xb3sito em conta - Banco do Brasil'), (b'702', b'Dep\xc3\xb3sito em conta - HSBC')]),
        ),
    ]
