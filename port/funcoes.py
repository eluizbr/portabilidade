# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

from datetime import timedelta,datetime,date
import datetime
from views import Cadastro, Portados, NaoPortados, PlanoCliente

'''
    Função retorna a diferença entre 2 datas
    ---> DESCREVA MAIS
'''
def diffDate(data1, data2):
   d1 = data1
   d2 = data2
   delta = d2-d1
   r = delta.days if (delta.days > 0) else "0"
   return r


'''
    Esta função retorna qual é o ID do cliente. Baseado nos seguintes dados:
    cod_cliente = Número 8 digitos inteiro (12345678)
    chave = Token UUID 32 digitos (d4697568956d47b9a2cafe0b17151c4a)

    Se a chave não existe retorna NONE.

'''

def pega_id_user(segredo):

    try:
        if len(segredo) == 8:
            cad = Cadastro.objects.get(cod_cliente=segredo)
            id_user = cad.id
            return id_user
        else:
            cad = Cadastro.objects.get(chave=segredo)
            id_user = cad.id
            return id_user

    except ObjectDoesNotExist:
        return None

'''
    Esta função retorna qual é o ID do cliente. Baseado nos seguintes dados:
    cod_cliente = Número 8 digitos inteiro (12345678)
    chave = Token UUID 32 digitos (d4697568956d47b9a2cafe0b17151c4a)

    Se a chave não existe retorna NONE.

'''

def checa_chave(key):

    if len(key) == 8:

      chave = Cadastro.objects.get(cod_cliente=key)
      chave = chave.cod_cliente
      chave = str(chave)
      return chave

    else:

      chave = Cadastro.objects.get(chave=key)
      chave = str(chave.chave)
      chave = chave.replace("-", "")
      return chave



'''
    Função retorna o CSP para número de 10 digitos
'''
def numero_10(numero):

    try:
        x = Portados.objects.get(numero=numero)
        p_numero = x.numero
        rn1 = x.rn1
        print rn1
        return rn1
    
    except ObjectDoesNotExist:

        try:
            prefixo = numero[0:6]
            x = NaoPortados.objects.get(prefixo=prefixo)
            prefixo = x.prefixo
            rn1 = x.rn1
            print rn1
            return rn1

        except ObjectDoesNotExist:
            return None


'''
    Função retorna o CSP para número de 11 digitos
'''
def numero_11(numero):

    try:
        x = Portados.objects.get(numero=numero)
        p_numero = x.numero
        rn1 = x.rn1
        return rn1
    
    except ObjectDoesNotExist:

        try:
            prefixo = numero[0:7]
            x = NaoPortados.objects.get(prefixo=prefixo)
            prefixo = x.prefixo
            rn1 = x.rn1
            return rn1

        except ObjectDoesNotExist:
            return None


'''
    Função checa se o cliente tem saldo.
'''
def checa_saldo(id_user):

    hoje = datetime.datetime.now()
    c = PlanoCliente.objects.get(cliente=id_user)
    saldo = c.consultas
    saldo = int(saldo)
    tipo = c.tipo
    tipo = int(tipo)

    expira = c.expira_em
    expira_y = int(expira.strftime("%Y"))
    expira_m = int(expira.strftime("%m"))
    expira_d = int(expira.strftime("%d"))

    diferenca = diffDate(date(expira_y,expira_m,expira_d),date(hoje.year,hoje.month,hoje.day))
    diferenca = int(diferenca)


    return saldo,tipo,diferenca




