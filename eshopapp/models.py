from django.db import models

# Create your models here.
class Producto(models.Model): 
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="eshopapp", null=True, blank=True)
    descripcion = models.TextField(default="descripcion")
    precio = models.FloatField()
    stock = models.IntegerField()
    TIPO_PRODUCTO_CHOICES = [
        (1, 'Normal'), 
        (2, 'Popular'), 
        (3, 'Promo')
    ]
    tipo = models.IntegerField(choices=TIPO_PRODUCTO_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre

class Pedido(models.Model): 
    usuario = models.CharField(max_length=50)
    nombreProducto = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self): 
        return self.usuario + " " + self.nombreProducto

