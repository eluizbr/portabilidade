# -*- coding: UTF-8 -*-
import uuid
from django.db import models
from django.contrib.auth.models import User

class NaoPortados(models.Model):
    operadora = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)
    prefixo = models.BigIntegerField()
    rn1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nao_portados'


class Portados(models.Model):
    numero = models.BigIntegerField()
    rn1 = models.IntegerField()
    data_hora = models.DateTimeField()
    op = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'portados'

class Prefixo(models.Model):
    ddd = models.IntegerField(blank=True, null=True)
    prefixo = models.IntegerField(unique=True, blank=True, null=True)
    inicial = models.IntegerField(blank=True, null=True)
    final = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    operadora = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)
    rn1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prefixo'
    def __unicode__(self):
        return unicode(self.prefixo)

class Plano(models.Model):

    plano = models.CharField(null=True,blank=True,max_length=255)
    valor = models.FloatField(blank=True, null=True, default=00.00)
    valor_consulta = models.FloatField(blank=True, null=True, default=00.00)
    consultas_gratis = models.IntegerField(blank=True, null=True,default=0)

    def __unicode__(self):
        return unicode(self.plano)


class Cdr(models.Model):

    cliente = models.ForeignKey('Cadastro')
    numero = models.CharField(max_length=30)
    prefixo = models.IntegerField()
    ddd = models.IntegerField()
    rn1 = models.IntegerField()
    operadora = models.CharField(max_length=30)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    portado = models.IntegerField(default=0)
    data = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    data_hora = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return unicode(self.numero)

class Cadastro(models.Model):

    PLANO = (
            ('Free', 'Free'),
            ('Premium', 'Premium'),
    )


    TIPO = (
        ('Pessoa Fisica', 'Pessoa Fisica'),
        ('Pessoa Juridica', 'Pessoa Juridica'),
    )

    user = models.OneToOneField(User, unique=True)
    tipo = models.CharField(u'Tipo', max_length=20, choices=TIPO)
    first_name = models.CharField(u'Nome', max_length=100)
    last_name = models.CharField(u'SobreNome', max_length=200)
    empresa = models.CharField(
        u'Nome fantasia', max_length=100, blank=True, null=True)
    cpf = models.CharField(u'CPF', max_length=20, blank=True, null=True, unique=True)
    cnpj = models.CharField(u'CNPJ', max_length=20, blank=True, null=True, unique=True)
    ie = models.CharField(
        u'Insc. Estadual', max_length=20, blank=True, null=True)
    telefoneF = models.CharField(
        u'Telefone Fixo', max_length=20, blank=True, null=True)
    telefoneM = models.CharField(
        u'Telefone Movel', max_length=20, blank=True, null=True)
    email = models.EmailField('Email', max_length=254, blank=True, null=True, unique=True)
    email_contato = models.EmailField(
        'Email contato', max_length=254, blank=True, null=True)
    nome = models.CharField(u'Nome', max_length=100, blank=True, null=True)
    endereco = models.CharField(u'Endereço', max_length=100, blank=True, null=True)
    numero = models.CharField(u'Número', max_length=100, blank=True, null=True)
    bairro = models.CharField(u'Bairro', max_length=100, blank=True, null=True)
    complemento = models.CharField(u'Complemento', max_length=100, blank=True, null=True)
    cidade = models.CharField(u'Cidade', max_length=100, blank=True, null=True)
    estado = models.CharField(u'Estado', max_length=100, blank=True, null=True)
    cep = models.CharField(u'CEP', max_length=10, default='00000-000')
    cod_cliente = models.IntegerField(u'Codigo do Cliente', unique=True)
    chave = models.UUIDField(default=uuid.uuid4, editable=False)
    plano = models.OneToOneField(Plano,default=1)

    def __unicode__(self):
        return unicode(self.user)

