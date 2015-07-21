from port.models import NaoPortados, Portados
from serializers import NaoPortadosSerializer,PortadosSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import port.funcoes

class NaoPortadosList(APIView):
	def get(self, request, format=None, numero=None, key=None):

		numero = request.GET['numero']
		segredo = request.GET['key']

		try:
			rn1,prefixo,operadora = port.funcoes.consulta_api(numero,segredo)
			rn1 = str(rn1)
			rn1 = rn1
			prefixo = prefixo
			operadora = operadora
			nao_portados = NaoPortados.objects.filter(rn1=rn1,prefixo=prefixo,operadora=operadora)
			print rn1,prefixo,operadora
			serializer = NaoPortadosSerializer(nao_portados, many=True)
		
		except ValueError:

			rn1,p_numero = port.funcoes.consulta_api(numero,segredo)
			rn1 = str(rn1)
			rn1 = rn1
			numero = p_numero
			print rn1,numero
			portados = Portados.objects.filter(rn1=rn1,numero=numero)
			serializer = PortadosSerializer(portados, many=True)

			

		
		return Response(serializer.data)
