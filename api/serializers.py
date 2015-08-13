from port.models import NaoPortados, Portados, Csp
from rest_framework import serializers

class NaoPortadosSerializer(serializers.ModelSerializer):
	class Meta:
		model = NaoPortados
		fields = ('operadora','tipo','prefixo','rn1')

class PortadosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Portados
		fields = ('rn1','numero')

class CspSerializer(serializers.ModelSerializer):
	class Meta:
		model = Csp
		fields = ('operadora', 'rn1', 'tipo')