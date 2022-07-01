from django.shortcuts import render,redirect
from .models import Cliente, Producto
from .forms import ProductoForm,ClienteForm

# Create your views here.
def index(request):
    productos=Producto.objects.all()
    datos={
        'productos':productos
    }
    return render(request,'index.html',datos)

def accesorios(request):
    return render(request,'accesorios.html')

def contacto(request):
    return render(request,'contacto.html')

def festivos(request):
    return render(request,'festivos.html')

def gato(request):
    return render(request,'gato.html')

def perro(request):
    return render(request,'perro.html')

def quienes_somos(request):
    return render(request,'quienes-somos.html')
def usuario(request):
    return render(request,'usuario.html')    
def listado(request):
    productos=Producto.objects.all()
    datos={
        'productos':productos
    }
    return render(request,'listado.html',datos)        
def listado_clientes(request):
    clientes=Cliente.objects.all()
    datos={
        'clientes':clientes
    }
    return render(request,'listado_clientes.html',datos)   

#crear productos
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
def eliminar_producto(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect(to='listado')

#Crear Cliente
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
def eliminar_cliente(request,id):
    cliente = Cliente.objects.get(rutCliente=id)
    cliente.delete()
    return redirect(to='listado_cliente')