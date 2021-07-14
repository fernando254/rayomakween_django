from webRayoMakween.models import Mecanico
from rest_framework import serializers

class MecanicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = ["nombre","descripcion","imagen"]