from seazone.models import Check,Limpeza
from rest_framework.viewsets import ModelViewSet
from seazone.api.serializers import Check_ClientesSerializer,LimpezaSerializer


class Check_ViewSet(ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = Check_ClientesSerializer

class Limpeza_ViewSet(ModelViewSet):
    queryset = Limpeza.objects.all()
    serializer_class = LimpezaSerializer
