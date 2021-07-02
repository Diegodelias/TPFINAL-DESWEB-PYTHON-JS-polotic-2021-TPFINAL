from django.urls import path , re_path
from django.conf.urls import url
from . import views

urlpatterns = [
   
    path('', views.index, name="index"),

    # re_path(r'^(?P<slug>[\w-]+)/$',views.detalle_producto, name ="detalle"),

    # path('detalle_producto/<slug:slug>',views.detalle_producto, name ="detalle_producto"),

    path('<int:producto_id>', views.detalle_producto , name ="detalle_producto"),

    path('nuevoProducto/', views.nuevoProducto, name="nuevoProducto"),

    path('actualizarProducto/<int:id>', views.actualizarProducto , name="actualizarProducto"),

    path('borrarProducto/<int:id>', views.borrarProducto , name="borrarProducto"),

    path('cargarCarrito/<int:producto_id>', views.cargarCarrito, name="cargarCarrito"),

    path('carrito/', views.carrito, name="carrito"),

    path('borrarItemCarrito/', views.borrarItemCarrito, name="borrarItemCarrito"),

    path('vaciarCarrito/', views.vaciarCarrito, name="vaciarCarrito"),

    path('finalizarCompra/', views.finalizarCompra, name="finalizarCompra"),


    path('Paginalogin/', views.Paginalogin, name="Paginalogin"),

    path('registro/', views.registro, name="registro"),

    path('logout/', views.logoutUsuario, name="logout"),


    path('filtro_categorias/<int:categoria_id>', views.filtro_categorias, name="filtro_categorias"),


    path('filtro_por_palabra/', views.filtro_por_palabra.as_view(), name="filtro_por_palabra"),


    
    path('AcercaDe/', views.AcercaDe, name="AcercaDe"),

    path('Contacto/', views.Contacto, name="Contacto"),


    path('confirmarBorrar/<int:id>', views.confirmarBorrar, name="confirmarBorrar"),




      


]
    

