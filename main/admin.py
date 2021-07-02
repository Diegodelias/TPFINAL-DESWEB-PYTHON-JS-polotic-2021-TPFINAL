from django.contrib import admin
from .models import *

# Register your models here.

from .models import *


class CarritoItemInline(admin.TabularInline):
    model = ItemCarrito
    raw_id_fields = ['product']

admin.site.register(Categoria)
admin.site.register(Producto)
# admin.site.register(Carrito)

admin.site.register(ItemCarrito)


@admin.register(Carrito)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'fecha_Alta','total']
    list_filter = ['usuario', 'fecha_Alta', 'total']
    inlines = [CarritoItemInline]