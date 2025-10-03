from rest_framework.viewsets import ModelViewSet
from iot.models import IoTData
from iot.serializers import IoTDataSerializer


class PingReciever(ModelViewSet):
    queryset = IoTData.objects.all()
    serializer_class = IoTDataSerializer
    allowed_methods = ['POST']
