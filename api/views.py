from port.models import NaoPortados
from serializers import NaoPortadosSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import port.funcoes

class NaoPortadosList(APIView):
	def get(self, request, format=None, numero=None, key=None):

		numero = request.GET['numero']
		segredo = request.GET['key']

		rn1 = port.funcoes.consulta_api(numero,segredo)
		rn1 = str(rn1)

		print rn1

		rn1 = rn1
		cadastro = NaoPortados.objects.filter(rn1=rn1)
		serializer = NaoPortadosSerializer(cadastro, many=True)
		return Response(serializer.data)
