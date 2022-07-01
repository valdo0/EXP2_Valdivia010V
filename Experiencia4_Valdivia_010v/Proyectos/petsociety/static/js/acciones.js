function Mover(obj)
{
  obj.style.opacity='1';
   
}

function MoverFuera(obj)
{
    obj.style.opacity='0.5';
    
    
}
function clase(obj)
{
  document.getElementById('modo').classList.toggle('dark');
}
        
function CambiaColor(a)
{
    a.style.background ='#DB5D16';
}
function Color(a)
{
  a.style.background ='white';
}
function CambiarMayusculas()
{
    var a = document.getElementById('nombre');
    a.value = a.value.toUpperCase();
}


$(document).ready(function(){
    
    $("#enviar").click(function(){
        

        $.get("https://apis.digital.gob.cl/fl/feriados/2022",function(data){

            $.each(data,function(i,item)
                {
                    $("#categorias").append("<tr><td>"+ item.nombre +
                    "</td><td>"+ item.fecha);
                  
                });


        });

    });
});

$(function(){
    $("#formulario").validate({
        rules:{
            nombre:"required",
            email: {
                  required: true,
                  email: true
              },
            telefono:"required",
            consulta:"required"

        },
        messages:{
            nombre:{
                required:'Debe ingresar su nombre',
                minlength:'Debe tener un minimo de 2 caracteres'
            },
            email:{
                required:'Debe ingresar su nombre',
                email:'formato de email no corresponde'                  },
            telefono:{
                required:'Debe ingresar una estatura',
                minlength:'Cantidad de digitos insuficientes'
            },
            consulta:{
                required:'Debe ingresar texto',
                minlength:'cantidad de caracteres insuficientes'
            }
            

        }
    })

});



$(function() 
{
  $("#formulario1").validate({
       rules: {
             nombre:"required",
              email: {
                  required: true,
                  email: true
              },
              contraseña:"required",
              fono: "required",
              fecha: "required",
              contraseña1: {
                  required: true,
                  equalTo: "#contraseña"
              }   
              
          }, 
      messages: {
          nombre:{
              required:'Debe ingresar un nombre',
              minlength:'Caracteres insuficientes'
          },
          email: {
              required: 'Ingresa tu correo electrónico',
              email: 'Formato de correo no válido'
          },
          contraseña: {
              required: 'Ingresa una contraseña',
              minlength: 'Caracteres insuficientes'
        
          },
          telefono:{
              required: 'Ingrese un número de celular',
              minlength: 'Cantidad de digitos insuficiente'
          },
          contraseña1: {
              required: 'Reingresa la contraseña',
              equalTo: 'Las contraseñas ingresadas no coinciden' ,
              minlength: 'Caracteres insuficientes'

          }
      }
  }); 
});

$(function() 
{
  $("#formulario_producto").validate({
       rules: {
              idProducto:"required",
              nombre:"required",
              precio: "required",
              marca: {
                        required:true,
                        max_length:2
            },
              imagen:"required",
              categoria:"required",
              
          }, 
      messages: {
          idProducto:{
              required:'Debe ingresar un id de producto'
          },
          nombre: {
              required: 'Ingresa nombre del producto'
          },
          precio: {
              required: 'Ingresa Precio'
        
          },
          marca:{
              required: 'Ingrese Marca',
              max_length:'No debe tener mas de 2 caracteres'
          },
          imagen: {
              required: 'Ingrese Imagen'

          },
          categoria: {
            required: 'Seleccione Categoria'

        }          
      }
  }); 
});