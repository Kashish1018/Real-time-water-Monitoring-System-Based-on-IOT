from rest_framework import serializers
from .models import IotData

class IotDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IotData
        exclude = ['password']
