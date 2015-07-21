from port.models import NaoPortados, Portados
from rest_framework import serializers

class NaoPortadosSerializer(serializers.ModelSerializer):
	class Meta:
		model = NaoPortados
		fields = ('operadora','tipo','prefixo','rn1')

class PortadosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Portados
		fields = ('rn1','numero')