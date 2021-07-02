from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.

class Categoria(models.Model):
    descripcion =  models.CharField(max_length= 255, null=True)

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    titulo = models.CharField(max_length= 255, null=True)
    # slug = models.SlugField( null=True)
    imagen = models.ImageField(default="noimage.png" , null=True ,blank=True)
    descripcion =  models.TextField(null=True ,blank=True)
    precio = models.FloatField()
    categoria = models.ForeignKey( Categoria , null=True , on_delete=models.CASCADE)
    fecha_alta = models.DateTimeField(default=now, editable=False)

    # def get_absolute_url(self):
    #     return reverse("main:detalle_producto", args=[self.slug])

    def __str__(self):
        return self.titulo

# class Carrito(models.Model):
#     titulo = models.CharField(max_length= 255, null=True , default='carrito')
#     usuario = models.ForeignKey( User , null=True , on_delete=models.CASCADE)
#     nombreusuario = usuario.name
#     productos = models.ManyToManyField( Producto )
#     #total carrito metodo que sume total producto
#     def __str__(self):
#         return self.titulo

    
#     def get_cart_items(self):
#         return self.productos.all()


# class ItemCarrito(models.Model):
#     producto =models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
#     carrito = models.ForeignKey("Carrito", on_delete=models.CASCADE , null=True )


# class Carrito(models.Model):
#     usuario = models.ForeignKey( User , null=True , on_delete=models.CASCADE)
#     # fecha_creacion = models.DateTimeField(default=now, editable=False)

#     items = models.ManyToManyField(Producto, through=ItemCarrito)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False , null=True)


    # def __str__(self):
    #     return self.fecha_creacion


class Carrito(models.Model):
    usuario = models.ForeignKey( User , null=True , on_delete=models.CASCADE)
    fecha_Alta = models.DateTimeField(auto_now_add=True,null=True)
    total = models.FloatField(default=0,blank=True)
   
    class Meta:
        ordering = ('-fecha_Alta',)
    def __str__(self):
        return f'Carrito {self.id}'
    def get_total_cost(self):
        return sum(item.get_precio() for item in self.items.all())
    def save(self, *args, **kwargs):
        self.total = self.get_total_cost()
        super(Carrito, self).save(*args, **kwargs)


class ItemCarrito(models.Model):
    order = models.ForeignKey(Carrito, related_name='items',on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Producto, related_name='order_items', on_delete=models.CASCADE,null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cantidad= models.PositiveIntegerField(default=1,null=True)
    
    
    def __str__(self):
        return str(self.id)
    def get_precio(self):
        return self.precio * self.cantidad



 

  

    