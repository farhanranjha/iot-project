from rest_framework import serializers
from iot.models import IoTData


class IoTDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoTData
        fields = '__all__'