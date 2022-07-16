from audioop import add
from urllib import request
from venv import create
from webbrowser import get
from django.shortcuts import render,redirect
from .models import Categoria, Cliente, DireccionEnvio, Orden, Producto,OrdenProducto,Estado
from .forms import ProductoForm,ClienteForm,CustomUserCreationForm,DireccionForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
def index(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_carrito_items
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}
        cartItems = orden['get_carrito_items']


    productos=Producto.objects.filter(destacado=True)
    datos={
        'productos':productos,
        'cartItems':cartItems
    }
    return render(request,'index.html',datos)

def accesorios(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_carrito_items
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}
        cartItems = orden['get_carrito_items']


    productos=Producto.objects.filter(accesorio=True)
    datos={
        'productos':productos,
        'cartItems':cartItems
    }
    return render(request,'accesorios.html',datos)

def contacto(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_carrito_items
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}
        cartItems = orden['get_carrito_items']


    productos=Producto.objects.all()
    datos={
        'productos':productos,
        'cartItems':cartItems
    }
    return render(request,'contacto.html',datos)

def festivos(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_carrito_items
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}
        cartItems = orden['get_carrito_items']


    productos=Producto.objects.all()
    datos={
        'productos':productos,
        'cartItems':cartItems
    }
    return render(request,'festivos.html',datos)

def gato(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_carrito_items
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}
        cartItems = orden['get_carrito_items']


    productos=Producto.objects.filter(categoria=2)
    datos={
        'productos':productos,
        'cartItems':cartItems
    }
    return render(request,'gato.html',datos)

def perro(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_carrito_items
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}
        cartItems = orden['get_carrito_items']


    productos=Producto.objects.filter(categoria=1)
    datos={
        'productos':productos,
        'cartItems':cartItems
    }
    return render(request,'perro.html',datos)

def quienes_somos(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_carrito_items
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}
        cartItems = orden['get_carrito_items']


    productos=Producto.objects.all()
    datos={
        'productos':productos,
        'cartItems':cartItems
    }
    return render(request,'quienes-somos.html',datos)
def usuario(request):
    
    data = {
        'formulario' : ClienteForm,
        'formulario2' : CustomUserCreationForm
        
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        formulario2= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid() and formulario2.is_valid():
            cliente = formulario.save(commit=False)
            cliente.user = formulario2.save()
            cliente.save()
            return redirect('index')

    return render(request,'usuario.html',data)    


@permission_required('app.view_producto')
def listado(request):
    productos=Producto.objects.all()
    datos={
        'productos':productos
    }
    return render(request,'listado.html',datos)  

@permission_required('app.view_cliente')          
def listado_clientes(request):
    clientes=Cliente.objects.all()
    datos={
        'clientes':clientes
    }
    return render(request,'listado_clientes.html',datos)   

#crear productos
@permission_required('app.add_producto')
def form_crear_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST,request.FILES)
        if producto_form.is_valid():
            producto_form.save()        #similar al insert
            return redirect('index')
    else:
        producto_form=ProductoForm()
    return render(request, 'form_producto.html', {'producto_form': producto_form})


#modificar productos
@permission_required('app.change_producto')
def form_mod_pro(request, id):
    producto = Producto.objects.get(idProducto=id)
    datos ={
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listado")
        datos["form"] = formulario 

            
    return render(request,'form_mod_pro.html',datos)

#eliminar productos
@permission_required('app.delete_producto')
def eliminar_producto(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect(to='listado')

#Crear Cliente
@permission_required('app.add_cliente')
def form_crear_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()        #similar al insert
            return redirect('index')
    else:
        cliente_form=ClienteForm()
    return render(request, 'form_cliente.html', {'cliente_form': cliente_form})

#modificar cliente
@permission_required('app.change_cliente')
def form_mod_cli(request, id):
    cliente = Cliente.objects.get(rutCliente=id)
    datos ={
        'form' : ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST,instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listado_clientes")
        datos["form"] = formulario           
    return render(request,'form_mod_cli.html',datos)    

#eliminar cliente 
@permission_required('app.delete_cliente')
def eliminar_cliente(request,id):
    cliente = Cliente.objects.get(rutCliente=id)
    cliente.delete()
    return redirect(to='listado_clientes')

#Carrito de compras
def canasta(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}

    context = {'items': items , 'orden':orden}
    return render(request,'canasta.html',context) 

def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        items = orden.ordenproducto_set.all()
    else:
        items = []
        orden = {'get_carrito_total':0,'get_carrito_items':0}


    direccion_form= DireccionForm(request.POST)
    if request.method=='POST':
        if direccion_form.is_valid():
            direccion=direccion_form.save()        #similar al insert     
            direccion.cliente=cliente
            direccion.orden=orden
            direccion.save()
            orden.completado=True
            estado=Estado.objects.get(estado='En Proceso')
            orden.estado=estado
            orden.save()
            orden , created = Orden.objects.get_or_create(cliente=cliente,completado=False)
            for item in items:
                producto=item.producto
                cantidad=item.cantidad
                producto.stock=(producto.stock-cantidad)
                producto.save()
            return redirect(to='index')
    else:
        direccion_form= DireccionForm()
    context = {'items': items , 'orden':orden,'direccion_form': direccion_form}    
    return render(request, 'checkout.html',context) 

     




def agregar_canasta(request,id):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        producto = Producto.objects.get(idProducto=id)
        orden,created = Orden.objects.get_or_create(cliente=cliente,completado=False)
        ordenproducto,created = OrdenProducto.objects.get_or_create(orden=orden,producto=producto)
        ordenproducto.cantidad = (ordenproducto.cantidad+1)
        if producto.stock >= ordenproducto.cantidad:
            ordenproducto.save()
        return redirect(to='canasta')
    else:
        return redirect(to='usuario')    

def quitar_canasta(request,id):
    
    cliente = request.user.cliente
    producto = Producto.objects.get(idProducto=id)
    orden,created = Orden.objects.get_or_create(cliente=cliente,completado=False)

    ordenProducto,created = OrdenProducto.objects.get_or_create(orden=orden,producto=producto)
    ordenProducto.cantidad = (ordenProducto.cantidad-1)
    ordenProducto.save()
    if ordenProducto.cantidad == 0:
        ordenProducto.delete()

    return redirect(to='canasta')

def pedidos(request):
    cliente = request.user.cliente
    direccion=DireccionEnvio.objects.filter(cliente=cliente)
    
    datos={
        'direcciones':direccion
    }

    return render(request,'pedidos.html',datos) 
