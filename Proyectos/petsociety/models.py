from tabnanny import verbose
from tkinter import image_names
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True,verbose_name='id de categoria')
    nombreCategoria=models.CharField(max_length=50,verbose_name='nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    idProducto=models.IntegerField(primary_key=True,verbose_name='id del producto')
    nombreProducto=models.CharField(max_length=50,verbose_name='nombre del producto')
    precio=models.IntegerField(verbose_name='precio del producto')
    marca=models.CharField(max_length=50,verbose_name='marca del producto')
    imagen=models.ImageField(verbose_name='imagen del producto')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreProducto

class Cliente(models.Model):
    rutCliente=models.CharField(max_length=13,primary_key=True,verbose_name='rut del cliente')
    nombreCliente=models.CharField(max_length=50,verbose_name='nombre del cliente')
    correo=models.EmailField(max_length=50,verbose_name='correo del cliente')
    telefono=models.IntegerField(verbose_name='telefono del cliente')