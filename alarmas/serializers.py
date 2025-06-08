
from rest_framework import serializers
from .models import Alarma

class AlarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarma
        fields = ['id','nombre_estacion','tipo_estacion','tech_area','activa']