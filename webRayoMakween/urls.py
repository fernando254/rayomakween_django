from django.contrib import admin
from django.urls import path
from .views import  index, galeria, consumir_api, cancelar, contratar, admin_usuario, formulario, agregar_imagen_galeria, contacto, registro, ficha, filtro_categoria, filtro_palabra_clave, filtro_nombre, filtro_cate, login, cerrar_sesion, crear_usuario, eliminar, buscar_modificar , modificar

urlpatterns = [
    
    path('',index, name='INDEX'),

    path('galeria/',galeria, name='GALERIA'),

    path('formulario/',formulario, name='FORMULARIO'),

    path('contacto/',contacto, name='CONTACTO'),

    path('registro/',registro, name='REGISTRO'),

    path('ficha/<id>/',ficha,name='FICHA'),

    path('filtro_categoria/',filtro_categoria,name='FILTRO_CATEGORIA'),

    path('filtro_palabra_clave/',filtro_palabra_clave,name='FILTRO_PALABRA_CLAVE'),

    path('filtro_nombre/',filtro_nombre,name='FILTRO_NOMBRE'),

    path('filtro_cate/<id>/',filtro_cate,name='FILTRO_CATE'),

    path('login/',login,name='LOGIN'),

    path('cerrar_sesion/',cerrar_sesion,name='CERRAR'),

    path('crear_usuario/',crear_usuario,name='CREARU'),

    path('eliminar/<id>/',eliminar,name='ELIMINAR'),

    path('buscar_modificar/<id>/',buscar_modificar,name='BUSCARM'),

    path('modificar/', modificar,name='MODIFICAR'),

    path('agregar_imagen_galeria/', agregar_imagen_galeria,name='AGREGARIMG'),

    path('contratar/<id>/', contratar,name='CONTRATAR'),

    path('admin_usuario/', admin_usuario,name='ADMINUSER'),

    path('cancelar/<id>/', cancelar,name='CANCELAR'),

    path('consumir_api/', consumir_api,name='API'),


]

