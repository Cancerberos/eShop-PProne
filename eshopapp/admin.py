from django.contrib import admin

# Register your models here.
from .models import Producto, Pedido

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Producto, ProductoAdmin)

class PedidoAdmin(admin.ModelAdmin): 
    readonly_fields = ("created", )

admin.site.register(Pedido, PedidoAdmin)