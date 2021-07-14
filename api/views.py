from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import MecanicoSerializers
from webRayoMakween.models import Mecanico

# Create your views here.

class MecanicoViewSet(generics.ListAPIView):
    queryset = Mecanico.objects.all()
    serializer_class = MecanicoSerializers