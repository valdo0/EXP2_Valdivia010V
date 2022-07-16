from msilib.schema import Class
from pyexpat import model
from tabnanny import verbose
from tkinter import CASCADE, image_names
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True,verbose_name='Id De Categoria')
    nombreCategoria=models.CharField(max_length=50,verbose_name='Nombre De La Categoria')

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    idProducto=models.IntegerField(primary_key=True,verbose_name='Id Del Producto')
    nombreProducto=models.CharField(max_length=50,verbose_name='Nombre Del Producto')
    precio=models.IntegerField(verbose_name='Precio Del Producto')
    marca=models.CharField(max_length=50,verbose_name='Marca Del Producto')
    imagen=models.ImageField(verbose_name='Imagen Del Producto')
    stock=models.IntegerField(verbose_name='Stock Del Producto',default='2')
    accesorio=models.BooleanField(default=False,verbose_name='Es Accesorio')
    destacado=models.BooleanField(default=False,verbose_name='Destacado')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreProducto

class Cliente(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    rutCliente=models.CharField(max_length=13,primary_key=True,verbose_name='Rut Del Cliente')
    nombreCliente=models.CharField(max_length=50,verbose_name='Nombre Del Cliente')
    correo=models.EmailField(max_length=50,verbose_name='Correo Del Cliente')
    telefono=models.IntegerField(verbose_name='Telefono Del Cliente')
    def __str__(self):
        return self.rutCliente  


class Estado(models.Model):
    estado=models.CharField(max_length=30,verbose_name='Estado De Pedido')
    def __str__(self):
        return str(self.estado)


class Orden(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Rut Cliente')        
    fechaOrden=models.DateField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    estado = models.ForeignKey(Estado,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Estado De Orden')
    def __str__(self):
        return str(self.id)

    @property
    def get_carrito_total(self):
        ordenitems = self.ordenproducto_set.all()
        total = sum([item.get_total for item in ordenitems])
        return total    

    @property
    def get_carrito_items(self):
        ordenitems = self.ordenproducto_set.all()
        total = sum([item.cantidad for item in ordenitems])
        return total    

class OrdenProducto(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,verbose_name='Id Producto')
    orden=models.ForeignKey(Orden,on_delete=models.CASCADE,verbose_name='Id De La Orden')
    cantidad=models.IntegerField(default=0,null=True,blank=True,verbose_name='Cantidad De roducto') 
    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total   
    def __str__(self):
        return str(self.producto)     

class DireccionEnvio(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL,blank=True,null=True)
    orden = models.ForeignKey(Orden,on_delete=models.SET_NULL,blank=True,null=True)
    direccion  = models.CharField(max_length=200,null=True)
    ciudad = models.CharField(max_length=200,null=True)
    comuna = models.CharField(max_length=200,null=True)
    codigoPostal= models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.direccion)    