from port.models import NaoPortados
from rest_framework import serializers

class NaoPortadosSerializer(serializers.ModelSerializer):
	class Meta:
		model = NaoPortados
		fields = ('operadora','tipo','prefixo','rn1')