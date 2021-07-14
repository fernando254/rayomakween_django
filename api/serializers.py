from django.db.models import fields
from webRayoMakween.models import Mecanico, Categoria
from rest_framework import serializers

class MecanicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = ["nombre","descripcion","imagen"]

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["nombre","imagen"]