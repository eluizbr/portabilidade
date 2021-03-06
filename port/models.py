# -*- coding: UTF-8 -*-
import uuid
from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import timedelta,date
import choices

data = datetime.datetime.now()
mes = data + timedelta(days=30)
hora = data + timedelta(hours=1)
hora = hora.strftime("%H:%M:%S")

class Cadastro(models.Model):

    PLANO = (
            ('Free', 'Free'),
            ('Premium', 'Premium'),
    )


    TIPO = (
        ('Pessoa Fisica', 'Pessoa Fisica'),
        ('Pessoa Juridica', 'Pessoa Juridica'),
    )
    login = models.CharField(u'Login de acesso', max_length=30)
    senha = models.CharField(u'Senha', max_length=100)
    user = models.OneToOneField(User, unique=True)
    tipo = models.CharField(u'Tipo', max_length=20, choices=TIPO)
    first_name = models.CharField(u'Nome', max_length=100)
    last_name = models.CharField(u'SobreNome', max_length=200)
    empresa = models.CharField(
        u'Nome fantasia', max_length=100, blank=True, null=True)
    cpf = models.CharField(u'CPF', max_length=20, unique=True)
    cnpj = models.CharField(u'CNPJ', max_length=20, blank=True, null=True)
    ie = models.CharField(
        u'Insc. Estadual', max_length=20, blank=True, null=True)
    telefoneF = models.CharField(
        u'Telefone Fixo', max_length=20, blank=True, null=True)
    telefoneM = models.CharField(
        u'Telefone Movel', max_length=20, blank=True, null=True)
    email = models.EmailField('Email', max_length=254, unique=True)
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
    cod_cliente = models.CharField(u'Codigo do Cliente',max_length=100, unique=True)
    chave = models.UUIDField(default=uuid.uuid4, editable=False)
    plano = models.IntegerField(u'Plano', default=1)
    revenda = models.IntegerField(u'Revenda', default=0)
    cod_revenda = models.CharField(u'Codigo da Revenda',max_length=100,default='0')
    cache = models.IntegerField(u'Cache', default=0)

    def __unicode__(self):
        return unicode(self.user)

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

    TIPO = choices.TIPO_PLANO_CHOICES
    ESPECIAL = choices.PLANO_ESPECIAL_CHOICES


    plano = models.CharField(null=True,blank=True,max_length=255)
    descricao = models.CharField(null=True,blank=True,max_length=255)
    valor = models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2, default=00.00)
    valor_consulta = models.FloatField(blank=True, null=True, default=00.00)
    consultas_gratis = models.IntegerField(blank=True, null=True,default=0)
    taxas = models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2, default=00.00)
    tipo = models.CharField(max_length=200,choices=TIPO,default=1)
    especial = models.CharField(u'Plano',max_length=200,choices=ESPECIAL,default=0)
    cod_cliente = models.ManyToManyField(Cadastro, related_name="cliente",blank=True)
    
    def __unicode__(self):
        return unicode(self.plano)

class PortPlanoCodCliente(models.Model):
    plano = models.ForeignKey(Plano)
    cadastro = models.ForeignKey(Cadastro)

    class Meta:
        managed = False
        db_table = 'port_plano_cod_cliente'
        #unique_together = (('plano_id', 'cadastro_id'),)
    def __unicode__(self):
        return unicode(self.plano)


class Cdr(models.Model):

    cliente = models.ForeignKey('Cadastro')
    numero = models.CharField(max_length=30)
    prefixo = models.IntegerField()
    ddd = models.IntegerField()
    rn1 = models.IntegerField()
    retorno = models.IntegerField(default=0)
    operadora = models.CharField(max_length=30)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    portado = models.IntegerField(default=0)
    data = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    data_hora = models.DateTimeField(auto_now=True)
    valor = models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2)
    
    def __unicode__(self):
        return unicode(self.numero)

class Cache(models.Model):
    numero = models.CharField(max_length=30)
    hora = models.TimeField(auto_now=True)
    cache = models.TimeField()
    cliente = models.IntegerField(default=0)


class PlanoCliente(models.Model):

    TIPO = choices.TIPO_PLANO_CHOICES
    CACHE = choices.CACHE_CHOICES
    RETORNO = choices.RETORNO_CHOICES

    #cliente = models.IntegerField(u'Cliente', default=1, unique=True)
    cliente = models.ForeignKey(Cadastro)
    plano = models.IntegerField(u'Plano', default=1)
    nome_plano = models.CharField(u'Nome do Plano',max_length=255)
    consultas = models.IntegerField(blank=True, null=True,default=0)
    consultas_gratis = models.IntegerField(blank=True, null=True,default=0)
    criado_em = models.DateTimeField(default=data)
    expira_em = models.DateTimeField(default=mes)
    tipo = models.CharField(max_length=200,choices=TIPO,default=1)
    cache = models.CharField(u'Cache habilitado',max_length=1,choices=CACHE,default=0)
    tempo = models.IntegerField(u'Tempo do cache em minutos',default=60)
    ddd = models.IntegerField(u'DDD', blank=True, null=True, default=31)
    aviso_email = models.BooleanField(u'Aviso por email', default=0)
    saldo_baixo = models.BooleanField(u'Saldo baixo', default=0)
    aviso_saldo = models.IntegerField(blank=True, null=True,default=250)
    sem_saldo = models.BooleanField(u'Sem saldo', default=0)
    retorno = models.CharField(u'Retorno',max_length=5,choices=RETORNO,default=1)

    def __unicode__(self):
        return unicode(self.plano)


class Retorno(models.Model):

    TIPO = choices.TIPO_MEIO_PAGAMENTO_CHOICES
    CODIGO = choices.CODIGO_PAGAMENTO_CHOICES
    STATUS = choices.STATUS_CHOICES
    # Referencia dos campos: https://pagseguro.uol.com.br/v3/guia-de-integracao/consulta-de-transacoes-por-codigo.html
    cliente = models.ForeignKey(Cadastro,blank=True)
    date = models.DateTimeField()
    lastEventDate = models.DateTimeField()
    code = models.CharField(max_length=200)
    reference = models.CharField(max_length=200)
    status = models.CharField(max_length=200,choices=STATUS,default=1)
    paymentMethod = models.CharField(max_length=200,choices=TIPO,default=1)
    paymentMethodCode = models.CharField(max_length=200,choices=CODIGO,default=101)
    grossAmount = models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2)
    discountAmount = models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2)
    netAmount = models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2)
    extraAmount = models.DecimalField(blank=True, null=True, max_digits=10,decimal_places=2)
    item = models.CharField(max_length=200)
    id_plano = models.IntegerField()
    controle = models.IntegerField(default=0)
    consultas = models.IntegerField(default=0)
    email = models.EmailField(default='email@email.com')
    name = models.CharField(max_length=255,default=1)
    phone = models.CharField(max_length=20,default=1)

    

    def __unicode__(self):
        return unicode(self.status)

class Csp(models.Model):
    operadora = models.CharField(max_length=255, blank=True, null=True)
    rn1 = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.rn1)

    class Meta:
        managed = False
        db_table = 'csp'

class CspRetorno(models.Model):
    user = models.IntegerField(blank=True, null=True)
    csp = models.IntegerField(u'CSP de origem',blank=True, null=True, unique=True)
    retorno = models.IntegerField(u'CSP de retorno',blank=True, null=True)
    # operadora = models.CharField(max_length=255,default=0)
    # tipo = models.CharField(max_length=30,default=0)

    def __unicode__(self):
        return unicode(self.retorno)

class SipBuddies(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=250)
    accountcode = models.CharField(max_length=30, blank=True, null=True)
    amaflags = models.CharField(max_length=1, blank=True, null=True)
    callgroup = models.CharField(max_length=30, blank=True, null=True)
    callerid = models.CharField(max_length=50, blank=True, null=True)
    canreinvite = models.CharField(max_length=3, blank=True, null=True)
    context = models.CharField(max_length=250, blank=True, null=True)
    defaultip = models.CharField(max_length=15, blank=True, null=True)
    dtmfmode = models.CharField(max_length=7, blank=True, null=True)
    fromuser = models.CharField(max_length=50, blank=True, null=True)
    fromdomain = models.CharField(max_length=31, blank=True, null=True)
    host = models.CharField(max_length=31, default='dynamic')
    incominglimit = models.CharField(max_length=2, blank=True, null=True)
    outgoinglimit = models.CharField(max_length=2, blank=True, null=True)
    insecure = models.CharField(max_length=4, blank=True, null=True)
    language = models.CharField(max_length=2, blank=True, null=True)
    mailbox = models.CharField(max_length=50, blank=True, null=True)
    md5secret = models.CharField(max_length=32, blank=True, null=True)
    nat = models.CharField(max_length=5, blank=True, null=True)
    permit = models.CharField(max_length=95, blank=True, null=True)
    deny = models.CharField(max_length=95, blank=True, null=True)
    pickupgroup = models.CharField(max_length=30, blank=True, null=True)
    port = models.CharField(max_length=5)
    qualify = models.CharField(max_length=4, blank=True, null=True, default='yes')
    useragent = models.CharField(max_length=255, blank=True, null=True)
    restrictcid = models.CharField(max_length=3, blank=True, null=True)
    lastms = models.IntegerField(blank=True, null=True)
    rtptimeout = models.CharField(max_length=3, blank=True, null=True)
    rtpholdtimeout = models.CharField(max_length=3, blank=True, null=True)
    fullcontact = models.CharField(max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=6)
    username = models.CharField(max_length=30)
    allow = models.CharField(max_length=100, blank=True, null=True)
    disallow = models.CharField(max_length=100, blank=True, null=True)
    regseconds = models.IntegerField()
    ipaddr = models.CharField(max_length=15)
    cliente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sip_buddies'