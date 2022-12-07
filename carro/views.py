from django.shortcuts import render, redirect
from .carro import carro
from eshopapp.models import Producto, Pedido

def agregarProducto(request, productoId): 
    Carro = carro(request)
    producto = Producto.objects.get(id = productoId)
    Carro.agregar(producto)
    return redirect("index")

def restarProducto(request, productoId): 
    Carro = carro(request)
    producto = Producto.objects.get(id = productoId)
    Carro.restar(producto)
    return redirect("index")

def limpiarCarro(request): 
    Carro = carro(request)
    Carro.limpiarCarro()
    return redirect("index")

def carrito(request): 
    return render (request, "carro.html")

def okPedido(request): 
    if request.user.is_authenticated: 
        ##Guardar los datos del pedido en la tabla Pedidos
        for key, value in request.session["carro"].items(): 
            usuario = request.user
            nombreProducto = value["nombre"]
            precio = value["precio"]
            cantidad = value["cantidad"]
            pedido = Pedido.objects.create(usuario = usuario, nombreProducto = nombreProducto, precio = precio, cantidad = cantidad)
        
        limpiarCarro(request)

        return render(request, "pedido.html")
    else: 
        return render(request, "authenticar.html")

