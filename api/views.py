from port.models import NaoPortados, Portados, Csp
from serializers import NaoPortadosSerializer,PortadosSerializer,CspSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import port.funcoes

class ConsultaApi(APIView):
	def get(self, request, format=None, numero=None, key=None):

		numero = request.GET['numero']
		segredo = request.GET['key']

		valor = Portados.objects.filter(numero=numero)

		if valor:
			rn1,p_numero = port.funcoes.consulta_rest(numero,segredo)
			rn1 = str(rn1)
			rn1 = rn1
			p_numero = p_numero
			portados = Csp.objects.all().filter(rn1=rn1)
			serializer = CspSerializer(portados, many=True)	
			return Response(serializer.data)

		else:
			rn1,prefixo,operadora = port.funcoes.consulta_rest(numero,segredo)
			rn1 = str(rn1)
			rn1 = rn1
			prefixo = prefixo
			operadora = operadora
			nao_portados = Csp.objects.all().filter(rn1=rn1)
			serializer = CspSerializer(nao_portados, many=True)	
			return Response(serializer.data)


		# if valor:
		# 	rn1,p_numero = port.funcoes.consulta_rest(numero,segredo)
		# 	rn1 = str(rn1)
		# 	rn1 = rn1
		# 	p_numero = p_numero
		# 	portados = Portados.objects.filter(rn1=rn1,numero=p_numero)
		# 	serializer = PortadosSerializer(portados, many=True)	
		# 	return Response(serializer.data)

		# else:
		# 	rn1,prefixo,operadora = port.funcoes.consulta_rest(numero,segredo)
		# 	rn1 = str(rn1)
		# 	rn1 = rn1
		# 	prefixo = prefixo
		# 	operadora = operadora
		# 	nao_portados = NaoPortados.objects.filter(rn1=rn1,prefixo=prefixo,operadora=operadora)
		# 	serializer = NaoPortadosSerializer(nao_portados, many=True)	
		# 	return Response(serializer.data)