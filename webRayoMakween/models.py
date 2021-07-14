from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=25)
    imagen = models.ImageField(upload_to='cate',null=True)

    def __str__(self):
        return self.nombre


class Mecanico(models.Model):
    nombre = models.CharField(primary_key=True,max_length=25)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='mecanicos',default='mecanicos/no_hay_imagen.jpg')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    publicar = models.BooleanField(default=False)
    comentario = models.TextField(default='--')
    usuario = models.CharField(max_length=45,default='--')
    dueno = models.CharField(max_length=45,default='--')

    def __str__(selft):
        return selft.nombre


class Galeria(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='galeria')
    mecanico = models.ForeignKey(Mecanico,on_delete=models.CASCADE)
    
    def __str__(selft):
        return "Numero:"+str(selft.auto_inc) 
