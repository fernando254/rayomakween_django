
from django.http import response
from django.shortcuts import render
#IMPORTAMOS LA TABLA
from .models import Categoria, Galeria, Mecanico

#importar tablaa user desde administrador
from django.contrib.auth.models import User

# importar libreria de login de acceso
from django.contrib.auth import authenticate, logout, login as login_aut

#agregar la libreria de decoradores (limitar el ingreso)
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.



def crear_usuario(request):
    mensaje=''
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        usuario = request.POST.get("txtUsuario")
        pass1 = request.POST.get("txtPass1")

        try:
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.username = usuario
            usu.set_password(pass1)

            usu.save()
            mensaje = "usuario almacenado"
        except:
            mensaje = "no pudo almacenar el usuario"
    datos = {"mensaje":mensaje}
    return render(request,"crear_usuario.html",datos)

def cerrar_sesion(request):
    logout(request)
    categorias = Categoria.objects.all()
    datos = {"categorias": categorias}
    return render(request,"index.html",datos)

def login(request):
    mensaje=''
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=usuario,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            # ir al index
            categorias = Categoria.objects.all()
            datos = {"categorias": categorias}
            return render(request,"index.html",datos)
        else:
            mensaje ="usuario o contraseña incorrecta"
            
    datos = {"mensaje":mensaje}
    return render(request,"login.html",datos)

def filtro_nombre(request):
    mecanicos = Mecanico.objects.all()
    cant = Mecanico.objects.all().count()
    if request.POST:
        nombre = request.POST.get("txtNombre")
        # el metodo filter permite generar el filtro de los objetos
        mecanicos = Mecanico.objects.filter(nombre=nombre).filter(publicar=True)
        # el metodo count efectua el conteo de los registros por la condicion
        cant = Mecanico.objects.filter(nombre=nombre).filter(publicar=True).count()

    categorias = Categoria.objects.all()
    datos = {"mecanicos":mecanicos,"categorias":categorias, "cantidad":cant}
    return render(request,"galeria.html",datos)

def filtro_palabra_clave(request):
    mecanicos = Mecanico.objects.all()
    cant = Mecanico.objects.all().count()
    if request.POST:
        desc = request.POST.get("txtDesc")
        # agregando contains efectue link sobre el campo
        mecanicos = Mecanico.objects.filter(descripcion__contains=desc).filter(publicar=True)
        cant = Mecanico.objects.filter(descripcion__contains=desc).filter(publicar=True).count()

    categorias = Categoria.objects.all()
    datos = {"mecanicos":mecanicos,"categorias":categorias,"cantidad":cant}
    return render(request,"galeria.html",datos)

def filtro_categoria(request):
    mecanicos = Mecanico.objects.all()
    cant = Mecanico.objects.all().count()
    if request.POST:
        cate = request.POST.get("cboCategoria")
        # buscar el objeto asociado al campo clave
        obj_cate = Categoria.objects.get(nombre=cate)
        # filtramos por entidad encontrada
        mecanicos = Mecanico.objects.filter(categoria=obj_cate).filter(publicar=True)
        cant = Mecanico.objects.filter(categoria=obj_cate).filter(publicar=True).count()

    categorias = Categoria.objects.all()
    datos = {"mecanicos":mecanicos,"categorias":categorias, "cantidad":cant}
    return render(request,"galeria.html",datos)

def filtro_cate(request,id):
    # buscar el objeto asociado al campo clave
    obj_cate = Categoria.objects.get(nombre=id)
    # filtramos por entidad encontrada
    mecanicos = Mecanico.objects.filter(categoria=obj_cate).filter(publicar=True)
    cant = Mecanico.objects.filter(categoria=obj_cate).filter(publicar=True).count()

    categorias = Categoria.objects.all()
    datos = {"mecanicos":mecanicos,"categorias":categorias, "cantidad":cant}
    return render(request, "galeria.html",datos)

def ficha(request,id):
    mecanico = Mecanico.objects.filter(publicar=True).get(nombre=id)
    datos = {"mecanico":mecanico}
    galeria = Galeria.objects.filter(mecanico=mecanico)
    datos["galeria"]= galeria
    return render(request,"ficha.html",datos)

def index(request):
    categorias = Categoria.objects.all()
    mecanicos = Mecanico.objects.filter(publicar=True).order_by('nombre')[:3]
    datos = {"categorias": categorias, "mecanicos": mecanicos}
    return render(request,"index.html",datos)

def galeria(request):
    mecanicos = Mecanico.objects.filter(publicar=True)
    cant = Mecanico.objects.filter(publicar=True).count()
    categorias = Categoria.objects.all()
    datos = {"mecanicos":mecanicos,"categorias":categorias,"cantidad":cant}
    return render(request,"galeria.html",datos)

def contacto(request):
    return render(request,"contacto.html")

def formulario(request):
    return render(request,"formulario.html")

@login_required(login_url= '/login/')
@permission_required('webRayoMakween.add_mecanico', login_url='/login/')
def registro(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        desc = request.POST.get("txtDesc") 
        imagen = request.FILES.get("txtImg")
        cate = request.POST.get("cboCategoria")  
        obj_cate = Categoria.objects.get(nombre=cate) # buscando objeto categoria
        mec = Mecanico()
        mec.nombre = nombre,
        mec.descripcion = desc,
        mec.categoria = obj_cate
        mec.usuario = request.user.username
        if imagen is not None:
            mec.imagen = imagen
        
        mec.save()
        mensaje="Guardado"

    categorias = Categoria.objects.all()  #ES LO MISMO QUE SELECT * FROM CATEGORIA
    mecanicos = Mecanico.objects.filter(usuario=request.user.username)
    cantidad = Mecanico.objects.filter(usuario=request.user.username).count()
    datos = {"cate": categorias,"mensaje":mensaje,"mecanicos":mecanicos, "cant":cantidad}
    return render(request,"registro.html",datos)

@login_required(login_url= '/login/')
@permission_required('webRayoMakween.delete_mecanico', login_url='/login/')
def eliminar(request,id):
    mensaje=''
    try:
        mec = Mecanico.objects.get(nombre=id)
        mec.delete()
        mensaje = "Mecanico Eliminado"
    except:
        mensaje = "No Existe el Mecanico"

    categorias = Categoria.objects.all()  #ES LO MISMO QUE SELECT * FROM CATEGORIA
    mecanicos = Mecanico.objects.filter(usuario=request.user.username)
    datos = {"cate": categorias,"mensaje":mensaje,"mecanicos":mecanicos}
    return render(request,"registro.html",datos)

@login_required(login_url= '/login/')
@permission_required('webRayoMakween.view_mecanico', login_url='/login/')
def buscar_modificar(request,id):
    mensaje =''
    try:
        mec = Mecanico.objects.get(nombre=id)
        categorias = Categoria.objects.all()  #ES LO MISMO QUE SELECT * FROM CATEGORIA
        datos = {"cate": categorias,"mecanico":mec}
        return render(request,"modificar.html",datos)
    except:
        mensaje = "No existe mantencion"

    categorias = Categoria.objects.all()  #ES LO MISMO QUE SELECT * FROM CATEGORIA
    mecanicos = Mecanico.objects.filter(usuario=request.user.username)
    datos = {"cate": categorias,"mensaje":mensaje,"mecanicos":mecanicos}
    return render(request,"registro.html",datos)

@login_required(login_url= '/login/')
@permission_required('webRayoMakween.change_mecanico', login_url='/login/')
def modificar(request):
    mensaje="" 
    if request.POST:
        nombre = request.POST.get("txtNombre")
        desc = request.POST.get("txtDesc")
        imagen = request.FILES.get("txtImagen")
        cate = request.POST.get("cboCategoria")

        obj_cate = Categoria.objects.get(nombre=cate)

        try:

            mec = Mecanico.objects.get(nombre=nombre)
            mec.descripcion = desc
            mec.categoria = obj_cate
            mec.comentario = '--'
            if imagen is not None:
                mec.imagen = imagen
            mec.save()
            mensaje = "Modifico Mantencion" + nombre
        except:
            mensaje = "No Modifico Mantencion"

    categorias = Categoria.objects.all()  #ES LO MISMO QUE SELECT * FROM CATEGORIA
    mecanicos = Mecanico.objects.filter(usuario=request.user.username)
    datos = {"cate": categorias,"mensaje":mensaje,"mecanicos":mecanicos}
    return render(request,"registro.html",datos)

@login_required(login_url= '/login/')
@permission_required('webRayoMakween.add_galeria', login_url='/login/')
def agregar_imagen_galeria(request):
    mensaje =""
    if request.POST:
        nombre_mecanico = request.POST.get("txtMecanico")
        imagen = request.FILES.get("txtImagen")
        obj_mecanico = Mecanico.objects.get(nombre=nombre_mecanico)

        gale = Galeria()
        gale.imagen = imagen
        gale.mecanico = obj_mecanico
        gale.save()
        mensaje = "Agrego imagen a Mecanico"+ nombre_mecanico

    categorias = Categoria.objects.all()  #ES LO MISMO QUE SELECT * FROM CATEGORIA
    mecanicos = Mecanico.objects.filter(usuario=request.user.username)
    datos = {"cate": categorias,"mensaje":mensaje,"mecanicos":mecanicos}
    return render(request,"registro.html",datos)
    

@login_required(login_url= '/login/')
def contratar(request,id):
    try:
        mec = Mecanico.objects.filter(publicar=True).get(nombre=id)
        mec.dueno = request.username
        mec.publicar = False
        mec.comentario = "contratado"
        mec.save()
        mensaje = "contratado"
    except:
        mensaje = "no encontrado"

    mecanico = Mecanico.objects.get(nombre=id)
    datos = {"mecanico":mecanico}
    galeria = Galeria.objects.filter(mecanico=mecanico)
    datos["galeria"]= galeria
    datos["mensaje"]= mensaje
    return render(request,"ficha.html",datos)


@login_required(login_url= '/login/')
def admin_usuario(request):
    mecanicos = Mecanico.objects.filter(dueno=request.user.username)
    datos = {"mecanicos":mecanicos}
    return render(request,"admin_usuario.html",datos)

@login_required(login_url= '/login/')
def cancelar(request,id):
    mensaje =""
    try:
        mec = Mecanico.objects.filter(publicar=True).get(nombre=id)
        mec.dueno ='--'
        mec.comentario ='--'
        mec.save()
        mensaje = "Mantencion Cancelada"
    except:
        mensaje = "No puede volver atras"

    mecanicos = Mecanico.objects.filter(dueno=request.user.username)
    datos = {"mecanicos":mecanicos,"mensaje":mensaje}
    return render(request,"admin_usuario.html",datos)



import requests

def consumir_api(request):

    response = requests.get("http://127.0.0.1:8000/api/mecanicos/")
    mecanicos = response.json()

    response = requests.get("http://127.0.0.1:8000/api/categorias/")
    categorias = response.json()

    if request.POST:
        nombre = request.POST.get("txtNombre")
        response = requests.get("http://127.0.0.1:8000/api/buscar_mecanico/"+nombre+"/")
        mecanicos = response.json()

    contexto = {"mecanicos": mecanicos,"categorias":categorias}
    return render(request,"consumir_api.html",contexto)


  
