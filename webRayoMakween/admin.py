from django.contrib import admin
from .models import Categoria, Galeria, Mecanico

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Mecanico)
admin.site.register(Galeria)