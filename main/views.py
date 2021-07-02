from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect

from .models import *
from .forms import ProductoForm, CrearFormularioUsuario
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import usuario_no_autenticado, permitir_usuarios ,solo_Moderador
from django.contrib.auth.models import Group
from django.views.generic import ListView




# Create your views here.
# @login_required(login_url='main:Paginalogin')
# @permitir_usuarios(['moderador','usuario-comun','AnonymousUser'])
def index(request):
    if "sesion_carrito" not in request.session:
        request.session["sesion_carrito"] = []
    ultimos3 = Producto.objects.order_by('-fecha_alta' )[0:3]
    resto =  Producto.objects.order_by('-fecha_alta' )[3:10]
    return render(request, "paginas/principal.html" , {"productos":ultimos3 , "resto": resto , "sesion_carrito": request.session["sesion_carrito"] ,
    "lista_categorias": Categoria.objects.all(),
})


def AcercaDe(request):
     return render(request, "paginas/AcercaDe.html" )

def Contacto(request):
     return render(request, "paginas/Contacto.html" )

def confirmarBorrar(request,id):
    data = Producto.objects.get(id = id )
    return render(request, "paginas/confirmarBorrar.html",{
         "prodborrar": data
     } )


@usuario_no_autenticado
def Paginalogin(request):
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return redirect('main:index')
        else:
            messages.info(request, 'Nombre de usuario o password incorrectos')
        
    context = {}
    return render(request, "paginas/Paginalogin.html", context)

def logoutUsuario(request):
    logout(request)
    return redirect('main:Paginalogin')

@usuario_no_autenticado
def registro(request):
  

    form = CrearFormularioUsuario()
    if request.method == 'POST':
        form = CrearFormularioUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            usuarionombre = form.cleaned_data.get('username')

            group = Group.objects.get(name='usuario-comun')

            user.groups.add(group)


            messages.success(request, ' Se creo la cuenta para ' + usuarionombre)
            return redirect('main:Paginalogin')
    contexto = {'form': form}
    return render(request, "paginas/registro.html", contexto)

#     return render(request, "paginas/layout.html" , {
    
#     "sesion_carrito": request.session["sesion_carrito"]
# })

# def detalle_producto(request,slug):
#     data = Producto.objects.get(slug=slug)
#     # return HttpResponse(slug)
#     return render(request, "paginas/detalle_producto.html", {"producto":data})

# @login_required(login_url='main:Paginalogin')
# @solo_Moderador

# @permitir_usuarios(['moderador'])


def detalle_producto(request, producto_id):
    
    data = Producto.objects.get(id = producto_id )
    # return HttpResponse(slug)
    return render(request, "paginas/detalle_producto.html", {"producto":data,"lista_categorias": Categoria.objects.all(),
    
    })

# @login_required(login_url='main:Paginalogin')
@permitir_usuarios(['moderador'])
def nuevoProducto(request):
    form = ProductoForm()
    if request.method ==  'POST':
       # print('Print POST:' ,  request.POST)
       form = ProductoForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('/')
    
    context = {'form': form}
    return render(request , "paginas/nuevoProducto.html", context)
# @login_required(login_url='main:Paginalogin')
@permitir_usuarios(['moderador'])
def actualizarProducto(request, id):
    producto = Producto.objects.get(id= id)
    form = ProductoForm(instance=producto)
    
    
    if request.method == 'POST':
        form = ProductoForm(request.POST ,request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, ' El producto fue editado correctamente ' )
            return redirect('/')


    context = {'form': form , 'producto': producto , "lista_categorias": Categoria.objects.all()}
    return render(request , 'paginas/editarProducto.html', context)


# @login_required(login_url='main:Paginalogin')
@permitir_usuarios(['moderador'])
def borrarProducto(request, id):
    producto = Producto.objects.get(id= id)
    if request.method == "POST":
        producto.delete()
        messages.success(request, ' El producto fue eliminado ' )
        return redirect('/')

    context = {'item':producto}
    return render(request,"paginas/confirmarBorrar.html", context)
    



@login_required(login_url='main:Paginalogin')
@permitir_usuarios(['usuario-comun'])
def cargarCarrito(request,producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    for id in request.session["sesion_carrito"]:
        if id == producto_id:
            #existe el articulo
            messages.error(request, ' El producto  ya existe en el carrito ' )
            return redirect("main:index")  
            # return HttpResponseRedirect(reverse("main:index", args=(un_producto.id,)))            
    request.session["sesion_carrito"] += [producto_id]
    data = []
    for id in request.session["sesion_carrito"]:
       
        data.append(Producto.objects.get(id = id ))


    # return HttpResponseRedirect(reverse("sitio:articulo", args=(un_articulo.id,)))
    # return render(request, "paginas/carrito.html", {"producto":data ,
    # "sesion_carrito": request.session["sesion_carrito"]
    
    # })
    messages.success(request, ' El producto fue cargado en el carrito ' )
    return redirect("main:index") 

    
  

# @login_required(login_url='main:Paginalogin')
@login_required(login_url='main:Paginalogin')
@permitir_usuarios(['usuario-comun'])
def carrito(request):
    data = []
    for id in request.session["sesion_carrito"]:
       
        data.append(Producto.objects.get(id = id ))


    # return HttpResponseRedirect(reverse("sitio:articulo", args=(un_articulo.id,)))
    return render(request, "paginas/carrito.html", {"producto":data ,
    "sesion_carrito": request.session["sesion_carrito"]
    
    })
    # context={"sesion_carrito": request.session["sesion_carrito"]}
    # return render(request,"paginas/carrito.html", context)

# @login_required(login_url='main:Paginalogin')
@permitir_usuarios(['usuario-comun'])
def borrarItemCarrito(request):
    data = json.loads(request.body)
    productoId = data['productoId']
    accion = data['accion']
    print('Producto:',productoId)
    print('Accion:' ,accion)

    # usar para guardar carrito en modelo
    # usuario = request.user
    # producto =  Producto.object.get(id=productoId )
    # 
    if accion == "eliminar-item":
        print(request.session["sesion_carrito"])
        request.session["sesion_carrito"].remove(int(productoId))
        request.session.modified = True
    

  
    return JsonResponse('El item fue agregado', safe=False )
# @login_required(login_url='main:Paginalogin')
@permitir_usuarios(['usuario-comun'])
def vaciarCarrito(request):
    data = json.loads(request.body)
    accion = data['accion']
    if accion == "vaciar-carrito":
        request.session["sesion_carrito"].clear()
        request.session.modified = True
     
    return JsonResponse('Se vacio el carrito', safe=False )

# @login_required(login_url='main:Paginalogin')
@permitir_usuarios(['usuario-comun'])
def finalizarCompra(request):
   
    varusuario = request.user
 
    carritoFinal = Carrito.objects.create(usuario=varusuario)

    for idP in request.session["sesion_carrito"]:
        print(type(idP))
        productoFinal = Producto.objects.get(id = idP)
        print(type(productoFinal.id) )

        itemCarrito, fecha_Alta= ItemCarrito.objects.get_or_create(order= carritoFinal, product = productoFinal , precio = productoFinal.precio, )
        itemCarrito.save()

    carritoFinal.total = carritoFinal.get_total_cost()
    carritoFinal.save()
    request.session["sesion_carrito"].clear()
    request.session.modified = True
    messages.success(request, ' Se registro la compra ' )
    return redirect("main:index") 


def filtro_categorias(request, categoria_id):
    una_categoria = get_object_or_404(Categoria, id=categoria_id)
    queryset = Producto.objects.all()
    queryset = queryset.filter(categoria=una_categoria)
    return render(request,"paginas/resultadoBusqueda.html", {
        "lista_productos": queryset,
        "lista_categorias": Categoria.objects.all(),
        "categoria_seleccionada": una_categoria
    })



# def filtro_por_palabra(request):
#     qs = Producto.objects.all()
#     buscar_query= request.GET.get('buscar')
#     # buscar_query= 'Ninja'
#     # print(buscar_query)
#     if buscar_query != '' and buscar_query is not None:
#         qs = qs.filter(titulo__icontains = buscar_query)


#     context = {
#         'queryset': qs
#     }

#     return render(request, "resultadoBusquedaPalabra.html", context)



     
class filtro_por_palabra(ListView):
    model = Producto
    template_name = 'paginas/resultadoBusquedaPalabra.html'
    context_object_name ='productosfiltro'


    def get_context_data(self, **kwargs):
                # Call the base implementation first to get a context
                context = super(filtro_por_palabra, self).get_context_data(**kwargs)
                # Get the blog from id and add it to the context
                context['lista_Productos'] = Categoria.objects.all()
                return context
   

    def get_queryset(self):
        todosLosProductos = Producto.objects.all()
        query = self.request.GET.get('q')
        print(type(todosLosProductos))
        return todosLosProductos.filter(titulo__icontains = query).order_by('-fecha_alta') 

      