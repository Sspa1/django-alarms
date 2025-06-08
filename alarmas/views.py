from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from alarmas.models import Alarma 
from alarmas.serializers import AlarmaSerializer 

from rest_framework.generics import ListCreateAPIView

class AlarmaList(ListCreateAPIView):
    queryset = Alarma.objects.all()
    serializer_class = AlarmaSerializer
