from django.contrib import admin
from .models import Categoria,Producto,Cliente,Orden,OrdenProducto,Estado,DireccionEnvio
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(OrdenProducto)
admin.site.register(Estado)
admin.site.register(DireccionEnvio)