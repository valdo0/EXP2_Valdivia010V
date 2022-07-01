from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from .views import accesorios, form_crear_cliente, index,form_crear_producto,contacto,festivos,gato,perro,quienes_somos,usuario,listado,form_mod_pro,eliminar_producto,listado_clientes,form_mod_cli,eliminar_cliente

urlpatterns = [
    path('',index,name="index"),
    path('form_crear_producto/',form_crear_producto,name='form_crear_producto'),
    path('form_crear_cliente/',form_crear_cliente,name='form_crear_cliente'),
    path('accesorios/',accesorios,name='accesorios'),
    path('contacto/',contacto,name='contacto'),
    path('festivos/',festivos,name='festivos'),
    path('gato/',gato,name='gato'),
    path('perro/',perro,name='perro'),
    path('quienes_somos/',quienes_somos,name='quienes_somos'),
    path('usuario/',usuario,name='usuario'),
    path('listado/',listado,name='listado'),
    path('form_mod_pro/<id>',form_mod_pro,name='form_mod_pro'),
    path('eliminar_producto/<id>',eliminar_producto,name='eliminar_producto'),
    path('listado_clientes/',listado_clientes,name='listado_clientes'),
    path('form_mod_cli/<id>',form_mod_cli,name='form_mod_cli'),
    path('eliminar_cliente/<id>',eliminar_cliente,name='eliminar_cliente'),

]