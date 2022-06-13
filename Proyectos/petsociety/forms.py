from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Cliente, Producto


class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nombreProducto', 'precio', 'marca','imagen','categoria']
        labels ={
            'idProducto': 'Id', 
            'nombreProducto': 'Nombre', 
            'precio': 'precio', 
            'marca': 'Marca',
            'imagen': 'Imagen',
            'categoria': 'Categoria'
        }
        widgets={
            'idProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Id del producto', 
                    'id': 'idProducto'
                }
            ), 
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Producto', 
                    'id' : 'nombre'
                }
            ), 
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precio'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese marca',
                    'id':'marca'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen'
                }
            ),           
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }


#form de usuario
class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rutCliente', 'nombreCliente', 'correo', 'telefono']
        labels ={
            'rutCliente': 'Id', 
            'nombreCliente': 'Nombre', 
            'correo': 'Correo', 
            'telefono': 'Telefono',
        }
        widgets={
            'rutCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut del cliente', 
                    'id': 'rutCliente'
                }
            ), 
            'nombreCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre de cliente', 
                    'id' : 'nombre'
                }
            ), 
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ), 
            'telefono': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese telefono',
                    'id':'telefono'
                }
            )

        }