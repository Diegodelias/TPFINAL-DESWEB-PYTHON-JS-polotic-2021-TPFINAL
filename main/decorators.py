from django.http import HttpResponse
from django.shortcuts import redirect

def usuario_no_autenticado(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:index')
        else:

         return view_func(request, *args, **kwargs)
    return wrapper_func

def permitir_usuarios(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
           
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('No está autorizado a ver esta pagina')
        return wrapper_func
    return decorator

def solo_Moderador(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
        
        if group == 'moderador' :
            return redirect(redirect('main:actualizarProducto'))

        if group == 'usuario-comun':
            return view_func(request, *args, **kwargs )
    return wrapper_func

        
