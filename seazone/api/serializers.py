from rest_framework.serializers import ModelSerializer
from seazone.models import Check,Limpeza


class Check_ClientesSerializer(ModelSerializer):
    class Meta:
        model = Check
        fields = '__all__'

class LimpezaSerializer(ModelSerializer):
    class Meta:
        model = Limpeza
        fields = '__all__'
