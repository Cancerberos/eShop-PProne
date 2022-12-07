def importeTotalCarro(request): 
    total = 0
    cantidad = 0

    if "carro" in request.session.keys(): 
        for key, value in request.session["carro"].items(): 
            total = total + float(value["precio"])
            cantidad = cantidad + value["cantidad"]

    return {"importeTotalCarro": total, "cantidadProductos": cantidad}
