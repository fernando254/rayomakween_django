from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import MecanicoSerializers, CategoriaSerializers
from webRayoMakween.models import Categoria, Mecanico

# Create your views here.

class MecanicoViewSet(generics.ListAPIView):
    queryset = Mecanico.objects.all()
    serializer_class = MecanicoSerializers

class CategoriaViewSet(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class MecanicoBuscarViewSet(generics.ListAPIView):
    serializer_class = CategoriaSerializers
    def get_queryset(self):
        nom_mecanico = self.kwargs['nombre']
        return Mecanico.objects.filter(nombre= nom_mecanico)