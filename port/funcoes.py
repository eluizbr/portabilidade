# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

from datetime import timedelta,datetime,date
import datetime
from views import Cadastro, Portados, NaoPortados, PlanoCliente, CspRetorno
from django.conf import settings
from tasks import insert_cdr

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
def numero_10(numero,user_id):

    try:
        x = Portados.objects.get(numero=numero)
        p_numero = x.numero
        rn1 = x.rn1
        z = CspRetorno.objects.values_list('retorno').filter(csp=rn1)
        try:
            z = z[0]
        except IndexError:
            z = z
        if z:
            rn1 = z[0]
        return rn1
    
    except ObjectDoesNotExist:

        try:
            prefixo = numero[0:6]
            x = NaoPortados.objects.get(prefixo=prefixo)
            prefixo = x.prefixo
            operadora = x.operadora
            rn1 = x.rn1
            # z = str(rn1)
            # rn1 = z[3:]
            z = CspRetorno.objects.values_list('retorno').filter(csp=rn1)
            try:
                z = z[0]
            except IndexError:
                z = z
            if z:
                rn1 = z[0]
            return rn1

        except ObjectDoesNotExist:
            return None

def numero_10_rest(numero):

    try:
        x = Portados.objects.get(numero=numero)
        p_numero = x.numero
        rn1 = x.rn1
        return rn1,p_numero
    
    except ObjectDoesNotExist:

        try:
            prefixo = numero[0:6]
            x = NaoPortados.objects.get(prefixo=prefixo)
            prefixo = x.prefixo
            operadora = x.operadora
            rn1 = x.rn1
            return rn1,prefixo,operadora

        except ObjectDoesNotExist:
            return None


'''
    Função retorna o CSP para número de 11 digitos
'''
def numero_11(numero,user_id):

    try:
        x = Portados.objects.get(numero=numero)
        p_numero = x.numero
        rn1 = x.rn1
        z = CspRetorno.objects.values_list('retorno').filter(csp=rn1)
        try:
            z = z[0]
        except IndexError:
            z = z
        if z:
            rn1 = z[0]
        return rn1
    
    except ObjectDoesNotExist:

        try:
            prefixo = numero[0:7]
            x = NaoPortados.objects.get(prefixo=prefixo)
            prefixo = x.prefixo
            operadora = x.operadora
            rn1 = x.rn1
            z = CspRetorno.objects.values_list('retorno').filter(csp=rn1)
            try:
                z = z[0]
            except IndexError:
                z = z
            if z:
                rn1 = z[0]
            return rn1

        except ObjectDoesNotExist:
            return None

def numero_11_rest(numero):

    try:
        x = Portados.objects.get(numero=numero)
        p_numero = x.numero
        rn1 = x.rn1
        return rn1,p_numero
    
    except ObjectDoesNotExist:

        try:
            prefixo = numero[0:7]
            x = NaoPortados.objects.get(prefixo=prefixo)
            prefixo = x.prefixo
            operadora = x.operadora
            rn1 = x.rn1
            return rn1,prefixo,operadora

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


def consulta_api(numero,key):

    hoje = datetime.datetime.now()
    segredo = key
    segredo = str(segredo)

    ### Chama a função que checa o ID do usuário
    id_user = pega_id_user(segredo)
    
    if id_user == None:
        rn1 = 'error - Chave não autoriada'
        response = HttpResponse(rn1, content_type='text/plain')
        return response
    else:
        id_user = id_user

    ### Chama a função que checa o saldo do cliente
    saldo,tipo,diferenca = checa_saldo(id_user)

    if diferenca >= 30:
        PlanoCliente.objects.filter(cliente=id_user).update(consultas=0,plano=1,nome_plano='Escolha um plano',tipo=1)

    if (saldo <= 0) and (tipo == 1):

        rn1 = 'error - Sem credito'
        response = HttpResponse(rn1, content_type='text/plain')
        return response
    else:

        tamanho = len(numero)
        
        key = key
        key = str(key)
        chave = checa_chave(key)

        if key == chave:

            if tamanho <= 9:
                rn1 = 'error - somente aceito 10 e 11 digitos'
                response = HttpResponse(rn1, content_type='text/plain')
                return rn1           
            
            if tamanho == 10:

                ### Chama a função que checa retorna o CSP para números de 10 dígitos
                csp = numero_10(numero)
                if numero == None:
                    rn1 = 'error - numero ou prefixo nao existe'
                    response = HttpResponse(rn1, content_type='text/plain')
                    return rn1 
                else:
                    rn1 = csp

            if tamanho == 11:

                ### Chama a função que checa retorna o CSP para números de 11 dígitos
                csp = numero_11(numero)
                if csp == None:
                    rn1 = 'error - numero ou prefixo nao existe'
                    response = HttpResponse(rn1, content_type='text/plain')
                    return rn1  

                else:
                    rn1 = csp

            ### Chama a função que insere no CELERY, e o CELERY debita e insere no CDR
            insert_cdr.apply_async(kwargs={'request': chave, 'numero': numero},countdown=settings.TEMPO_ESPERA_CDR) 

            #response = HttpResponse(rn1, content_type='text/plain')
            return rn1

        else:

            rn1 = 0
            response = HttpResponse(rn1, content_type='text/plain')
            return rn1

def consulta_rest(numero,key):

    hoje = datetime.datetime.now()
    segredo = key
    segredo = str(segredo)

    ### Chama a função que checa o ID do usuário
    id_user = pega_id_user(segredo)
    
    if id_user == None:
        rn1 = 'error - Chave não autoriada'
        response = HttpResponse(rn1, content_type='text/plain')
        return response
    else:
        id_user = id_user

    ### Chama a função que checa o saldo do cliente
    saldo,tipo,diferenca = checa_saldo(id_user)

    if diferenca >= 30:
        PlanoCliente.objects.filter(cliente=id_user).update(consultas=0,plano=1,nome_plano='Escolha um plano',tipo=1)

    if (saldo <= 0) and (tipo == 1):

        rn1 = 'error - Sem credito'
        response = HttpResponse(rn1, content_type='text/plain')
        return response
    else:

        tamanho = len(numero)
        
        key = key
        key = str(key)
        chave = checa_chave(key)

        if key == chave:

            if tamanho <= 9:
                rn1 = 'error - somente aceito 10 e 11 digitos'
                response = HttpResponse(rn1, content_type='text/plain')
                return rn1           
            
            if tamanho == 10:

                ### Chama a função que checa retorna o CSP para números de 10 dígitos
                csp = numero_10_rest(numero)
                if numero == None:
                    rn1 = 'error - numero ou prefixo nao existe'
                    response = HttpResponse(rn1, content_type='text/plain')
                    return rn1 
                else:
                    rn1 = csp

            if tamanho == 11:

                ### Chama a função que checa retorna o CSP para números de 11 dígitos
                csp = numero_11_rest(numero)
                if csp == None:
                    rn1 = 'error - numero ou prefixo nao existe'
                    response = HttpResponse(rn1, content_type='text/plain')
                    return rn1  

                else:
                    rn1 = csp

            ### Chama a função que insere no CELERY, e o CELERY debita e insere no CDR
            #insert_cdr.apply_async(kwargs={'request': chave, 'numero': numero},countdown=settings.TEMPO_ESPERA_CDR) 

            #response = HttpResponse(rn1, content_type='text/plain')
            return rn1

        else:

            rn1 = 0
            response = HttpResponse(rn1, content_type='text/plain')
            return rn1

