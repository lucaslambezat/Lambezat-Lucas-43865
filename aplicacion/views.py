from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#-----------------------------------------------------------------------------------------

#VISTA PARA LA PÁGINA DE INICIO 
#Recupero todos los registros de la tabla de la BD asociada al modelo Post y los ordenarlos de acuerdo a la fecha de publicación.
#Solo se toman los últimos 4 posts. -> [:4]
#Se le pasa a la plantilla un diccionario con las útlimas 4 publicaciones para que las pueda usar al renderizarla en mi página de inicio.

def index(request):
    ultimos_posts = Post.objects.all().order_by('-fecha_public')[:4]    #El guión adelante del atributo invierte el orden. 
    return render(request, "aplicacion/index.html", {'ultimos_posts': ultimos_posts})


#VISTA PARA LA PÁGINA "ACERCA DE MÍ"

def about(request):
    return render(request, "aplicacion/about.html")


#------------------------------------------------------------------------------------------
#CLASES BASADAS EN VISTA PARA EL "CRUD" DE LOS EQUIPOS.
#Estas clases heredan de LoginRequiredMixin, que es una clase que asegura que el usuario esté autenticado antes de poder acceder a esta vista. 

class EquipoList(LoginRequiredMixin, ListView):
    model = Equipo

class EquipoCreate(LoginRequiredMixin, CreateView):
    model = Equipo
    fields = ['nombre', 'marca', 'sector', 'referencia']    #Especifico los campos del modelo a utilizar en el formulario.
    success_url = reverse_lazy('equipos')                   #Especifico la URL de redirección exitosa.

class EquipoDetail(LoginRequiredMixin, DetailView):
    model = Equipo

class EquipoUpdate(LoginRequiredMixin, UpdateView):
    model = Equipo
    fields = ['nombre', 'marca', 'sector', 'referencia']    #Especifico los campos del modelo a utilizar en el formulario.
    success_url = reverse_lazy('equipos')

class EquipoDelete(LoginRequiredMixin, DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipos')


#FUNCIONES PARA LA BÚSQUEDA DE LOS EQUIPOS EN LA BD DE ACUERDO A LA REFERENCIA.

#Se utiliza el decorador login_required al comienzo de la definición de funciones.
#El decorador asegura que solo los usuarios autenticados puedan acceder a esta vista.
#Si un usuario no está autenticado, será redirigido a la página de inicio de sesión.

#Esta primera vista simplemente renderiza una página de búsqueda con el formulario.

@login_required
def busquedaEquipo(request):

    return render (request, "aplicacion/equipo_busqueda.html")


#Esta segunda vista procesa la búsqueda de equipos y muestra los resultados en una página diferente.


@login_required
def buscarEquipo(request):

    if request.GET["referencia"]:   #Se verifica si se proporcionó alguna referencia con el parámetro GET.
        
        #Si es así, se procede a la búsqueda a partir de la referencia filtrando en la BD.

        referencia = request.GET['referencia']
        equipos = Equipo.objects.filter(referencia__icontains=referencia)
        return render(request, 
                      "aplicacion/equipo_resultados.html", 
                      {"referencia": referencia, "equipos":equipos})    #Se le pasan a la plantilla los diccionarios con los resultados para mostrar al renderizar la plantilla.
    
    else:
        
        #Si no se proporciona una referencia en la búsqueda, se renderiza la plantilla que indica que no se han ingresado datos.

        return render (request, "aplicacion/sin_datos.html")


#------------------------------------------------------------------------------------------
#CLASES BASADAS EN VISTA PARA EL "CRUD" DE LOS EMPLEADOS.
#Estas clases heredan de LoginRequiredMixin, que es una clase que asegura que el usuario esté autenticado antes de poder acceder a esta vista. 

class EmpleadoList(LoginRequiredMixin, ListView):
    model = Empleado

class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'rol', 'email', 'telefono']     #Especifico los campos del modelo a utilizar en el formulario.
    success_url = reverse_lazy('empleados')                         #Especifico la URL de redirección exitosa.

class EmpleadoDetail(LoginRequiredMixin, DetailView):
    model = Empleado

class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'rol', 'email', 'telefono']     #Especifico los campos del modelo a utilizar en el formulario.
    success_url = reverse_lazy('empleados')                         #Especifico la URL de redirección exitosa.

class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

#FUNCIONES PARA LA BÚSQUEDA DE LOS EMPLEADOS EN LA BD DE ACUERDO A LA REFERENCIA.

#Se utiliza el decorador login_required al comienzo de la definición de funciones.
#El decorador asegura que solo los usuarios autenticados puedan acceder a esta vista.
#Si un usuario no está autenticado, será redirigido a la página de inicio de sesión.

#Esta primera vista simplemente renderiza una página de búsqueda con el formulario.

@login_required
def busquedaEmpleado(request):

    return render (request, "aplicacion/empleado_busqueda.html")

#Esta segunda vista procesa la búsqueda de empleados y muestra los resultados en una página diferente.

@login_required
def buscarEmpleado(request):

    if request.GET["apellido"]:

        apellido = request.GET['apellido']
        empleados = Empleado.objects.filter(apellido__icontains=apellido)
        return render(request, 
                      "aplicacion/empleado_resultados.html", 
                      {"apellido": apellido, "empleados":empleados})
    else:

        return render (request, "aplicacion/sin_datos.html")


#------------------------------------------------------------------------------------------
#CLASES BASADAS EN VISTA PARA EL "CRUD" DE LOS MANTENIMIENTOS.

class MantenimientoList(LoginRequiredMixin, ListView):
    model = Mantenimiento

class MantenimientoCreate(LoginRequiredMixin, CreateView):
    model = Mantenimiento
    fields = ['numero_operacion', 'descripcion', 'planificado', 'fecha']
    success_url = reverse_lazy('mantenimientos')

class MantenimientoDetail(LoginRequiredMixin, DetailView):
    model = Mantenimiento

class MantenimientoUpdate(LoginRequiredMixin, UpdateView):
    model = Mantenimiento
    fields = ['numero_operacion', 'descripcion', 'planificado', 'fecha']
    success_url = reverse_lazy('mantenimientos')

class MantenimientoDelete(LoginRequiredMixin, DeleteView):
    model = Mantenimiento
    success_url = reverse_lazy('mantenimientos')

#FUNCIONES PARA LA BÚSQUEDA DE LOS MANTENIMIENTOS EN LA BD DE ACUERDO AL NÚMERO DE OPERACIÓN.

@login_required
def busquedaMantenimiento(request):

    return render (request, "aplicacion/mantenimiento_busqueda.html")

@login_required
def buscarMantenimiento(request):

    if request.GET["numero_operacion"]:

        numero_operacion = request.GET['numero_operacion']
        mantenimientos = Mantenimiento.objects.filter(numero_operacion__icontains=numero_operacion)
        return render(request, 
                      "aplicacion/mantenimiento_resultados.html", 
                      {"numero_operacion": numero_operacion, "mantenimientos":mantenimientos})
    else:

        return render (request, "aplicacion/sin_datos.html")


#------------------------------------------------------------------------------------------
#CLASES BASADAS EN VISTA PARA EL "CRUD" DE LOS POSTS.

class PostList(ListView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_public']
    success_url = reverse_lazy('posts')

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_public']
    success_url = reverse_lazy('posts')

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

#FUNCIONES PARA LA BÚSQUEDA DE LOS POSTS EN LA BD DE ACUERDO AL TÍTULO.

@login_required
def busquedaPost(request):

    return render (request, "aplicacion/post_busqueda.html")

@login_required
def buscarPost(request):

    if request.GET["titulo"]:

        titulo = request.GET['titulo']
        posts = Post.objects.filter(titulo__icontains=titulo)
        return render(request, 
                      "aplicacion/post_resultados.html", 
                      {"titulo": titulo, "posts":posts})
    else:

        return render (request, "aplicacion/sin_datos.html")

#------------------------------------------------------------------------------------------
#VISTA PARA EL INICIO DE SESIÓN


def login_request(request):
    if request.method == "POST":                                    #Se verifica que la solicitud sea de tipo POST
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():                                       #Se verifica si los datos proporcionados en el formulario son válidos.
            usuario = miForm.cleaned_data.get('username')           #Se obtiene el nombre de usuario ingresado en el formulario.
            clave = miForm.cleaned_data.get('password')             #Se obtiene la contraseña ingresada en el formulario.
            user = authenticate(username=usuario, password=clave)   #Se utiliza la función authenticate() para verificar los datos proporcionadas.
            
            #Si los datos del usuario son válidos, se devuelve el objeto de usuario autenticado.
            if user is not None:
                login(request, user)                                #Se inicia sesión con el usuario de "user".

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url    #Se intenta obtener la URL del avatar del usuario desde la base de datos.
                except:
                    avatar = '/media/avatares/default.png'                          #Si no se encuentra un avatar para el usuario, se establece un avatar por defecto.
                finally:
                    request.session['avatar'] = avatar

                return render(request, "aplicacion/index.html")                     #Se almacena la URL del avatar en la sesión del usuario
            
            #Si los datos del usuario no son válidas, se vuelve a mostrar el formulario con un mensaje de datos inválidos.
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    else:
        miForm = AuthenticationForm()
        return render(request, "aplicacion/login.html", {"form":miForm}) 


#------------------------------------------------------------------------------------------
#VISTA PARA REGISTRO DE USUARIO

def register(request):
    if request.method == 'POST':    #Se verifica que la solicitud sea de tipo POST
        form = RegistroUsuariosForm(request.POST) 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()     #Se guarda el usuario en la BD.
            return render(request, "aplicacion/index.html")     #Una vez que se registró se regresa a la página de inicio.
    else:
        form = RegistroUsuariosForm()   #Si se accede por primera vez, se renderiza la plantilla con el formulario creado RegistroUsuarios.

    return render(request, "aplicacion/registro.html", {"form": form})   



#------------------------------------------------------------------------------------------
#VISTA PARA EDITAR PERFIL


@login_required
def editarPerfil(request):
    usuario = request.user      #Se obtiene el objeto usuario que se encuentra logueado.
    if request.method == "POST":    #Se verifica que la solicitud sea de tipo POST, es decir, si se enviaron datos.
        form = UserEditForm(request.POST)       #Se crea una instancia del formulario a partir de los datos enviados.
        if form.is_valid():     
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()      #Se actualizan los datos del usuario y se guardan los cambios en la base de datos. 
            return render(request, "aplicacion/index.html")     #Finalizado el proceso, regresa a la página de inicio.
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})      #Si los datos no son válidos, se vuelve a renderizar el form.
    else:
        form = UserEditForm(instance=usuario)   #Si es la primera vez, se crea una instancia del formulario con los datos actuales del usuario logueado.
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})



#------------------------------------------------------------------------------------------
#VISTA PARA AGREGAR AVATAR


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #_________________ Esto es para borrar el avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: # Si esto es verdad quiere decir que hay un Avatar previo
                avatarViejo[0].delete()

            #_________________ Grabo avatar nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            #_________________ Almacenar en session la url del avatar para mostrarla en base
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/index.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})

