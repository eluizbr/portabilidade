# -*- coding: UTF-8 -*-

RETORNO_CHOICES = (
    ('1', 'CSP Completo'),
    ('2', 'Código de operadora apenas')
)


CACHE_CHOICES = (
    ('0', 'Desativado'),
    ('1', 'Ativado')
)

TIPO_PLANO_CHOICES = (
    ('0', 'Ilimitado'),
    ('1', 'normal')
)


STATUS_CHOICES = (
    ('1', 'Aguardando pagamento'),
    ('2', 'Em análise'),
    ('3', 'Pago'),
    ('4', 'Disponível'),
    ('5', 'Em disputa'),
    ('6', 'Devolvido'),
    ('7', 'Cancelado'),
    ('8', 'Valor devolvido'),
    ('9', 'Em contestação')
)


TIPO_MEIO_PAGAMENTO_CHOICES = (
    ('1', 'Cartão de crédito'),
    ('2', 'Boleto'),
    ('3', 'Débito online (TEF)'),
    ('4', 'Saldo PagSeguro'),
    ('5', 'Oi Paggo'),
    ('7', 'Depósito em conta')
)



CODIGO_PAGAMENTO_CHOICES = (
    ('101', 'Cartão de crédito Visa'),
    ('102', 'Cartão de crédito MasterCard'),
    ('103', 'Cartão de crédito American Express'),
    ('104', 'Cartão de crédito Diners'),
    ('105', 'Cartão de crédito Hipercard'),
    ('106', 'Cartão de crédito Aura'),
    ('107', 'Cartão de crédito Elo'),
    ('108', 'Cartão de crédito PLENOCard'),
    ('109', 'Cartão de crédito PersonalCard'),
    ('110', 'Cartão de crédito JCB'),
    ('111', 'Cartão de crédito Discover'),
    ('112', 'Cartão de crédito BrasilCard'),
    ('113', 'Cartão de crédito FORTBRASIL'),
    ('114', 'Cartão de crédito CARDBAN'),
    ('115', 'Cartão de crédito VALECARD'),
    ('116', 'Cartão de crédito Cabal'),
    ('117', 'Cartão de crédito Mais!'),
    ('118', 'Cartão de crédito Avista'),
    ('119', 'Cartão de crédito GRANDCARD'),
    ('120', 'Cartão de crédito Sorocred'),
    ('201', 'Boleto Bradesco'),
    ('202', 'Boleto Santander'),
    ('301', 'Débito online Bradesco'),
    ('302', 'Débito online Itaú'),
    ('303', 'Débito online Unibanco'),
    ('304', 'Débito online Banco do Brasil'),
    ('305', 'Débito online Banco Real'),
    ('306', 'Débito online Banrisul'),
    ('307', 'Débito online HSBC'),
    ('401', 'Saldo PagSeguro'),
    ('501', 'Oi Paggo'),
    ('701', 'Depósito em conta - Banco do Brasil'),
    ('702', 'Depósito em conta - HSBC'),

)
