from django.contrib import admin

# Register your models here.

from .models import Equipo, Mantenimiento, Empleado, Avatar

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Mantenimiento)
admin.site.register(Empleado)
admin.site.register(Avatar)