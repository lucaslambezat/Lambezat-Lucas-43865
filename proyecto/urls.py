from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from proyecto import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #Creo un path por aplicación. Para que todas las rutas relacionadas a esa aplicación las encuentre en un archivo.
    #Cada vez que encuentre una ruta que empiece por aplicación, busca esa ruta en este archivo. Dentro del paquete "aplicacion", el archivo "urls.py".
    path('aplicacion/', include('aplicacion.urls')),

    
]


urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)