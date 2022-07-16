from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Cliente, Producto, DireccionEnvio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nombreProducto', 'precio', 'marca','imagen','stock','accesorio','destacado','categoria']
        labels ={
            'idProducto': 'Id', 
            'nombreProducto': 'Nombre', 
            'precio': 'Precio', 
            'marca': 'Marca',
            'imagen': 'Imagen',
            'stock':'Stock',
            'accesorio': 'Accesorio',
            'destacado':'Destacado',
            'categoria': 'Categoria'
        }
        widgets={
            'idProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Id del producto', 
                    'id': 'idProducto',
                    'onfocus':'CambiaColor(this)',
                    'onfocusout':'Color(this)'
                }
            ), 
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Producto', 
                    'id' : 'nombre',
                    'onfocus':'CambiaColor(this)',
                    'onfocusout':'Color(this)'
                }
            ), 
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precio',
                    'onfocus':'CambiaColor(this)',
                    'onfocusout':'Color(this)'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese marca',
                    'id':'marca',
                    'onfocus':'CambiaColor(this)',
                    'onfocusout':'Color(this)'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen'
                }
            ),  
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese stock', 
                    'id': 'stock',
                    'onfocus':'CambiaColor(this)',
                    'onfocusout':'Color(this)'
                }
            ),
             'accesorio': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input',
                    'id': 'accesorio',
                }
            ),
            'destacado': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input',
                    'id': 'destacado',
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
            'rutCliente': 'Rut', 
            'nombreCliente': 'Nombre', 
            'correo': 'Correo', 
            'telefono': 'Telefono',
            'direccion': 'Direccion',
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
class CustomUserCreationForm(UserCreationForm):
    pass   

#form de direccion

class DireccionForm(forms.ModelForm):

    class Meta: 
        model= DireccionEnvio
        fields = ['direccion', 'ciudad', 'comuna', 'codigoPostal']
        labels ={
            'direccion': 'Direccion', 
            'ciudad': 'Ciudad', 
            'comuna': 'Comuna',
            'codigoPostal': 'Codigo Postal',
        }
        widgets={
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Direccion', 
                    'id': 'direccion'
                }
            ), 
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Ciudad', 
                    'id' : 'ciudad'
                }
            ), 
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Comuna', 
                    'id': 'comuna'
                }
            ), 
            'codigoPostal': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Codigo Postal',
                    'id':'codigoPostal'
                }
            )

        }
