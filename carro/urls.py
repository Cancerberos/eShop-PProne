from django.urls import path
from . import views

app_name = "carro"

urlpatterns = [
    path('', views.carrito, name = "carrito"), 
    path('agregar/<int:productoId>/', views.agregarProducto, name = "agregar"), 
    path('restar/<int:productoId>/', views.restarProducto, name = "restar"), 
    path('okpedido', views.okPedido, name = "okPedido"), 
]