class carro: 
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")

        if not carro:
            self.session["carro"] = {}
            self.carro = self.session["carro"]
        else:
            self.carro = carro

    def agregar(self, producto): 
        id = str(producto.id)

        if id not in self.carro.keys():
            self.carro[id] = {
                "producto_id": producto.id, 
                "nombre": producto.nombre, 
                "descripcion": producto.descripcion, 
                "precio": str(producto.precio), 
                "cantidad": 1, 
                "imagen": producto.imagen.url
            }
        else: 
            self.carro[id]["cantidad"] += 1
            self.carro[id]["precio"] = self.carro[id]["cantidad"] * producto.precio
        
        self.guardarCarro()

    def guardarCarro(self): 
        self.session["carro"] = self.carro
        self.session.modifed = True

    def eliminar(self, producto): 
        producto.id = str(producto.id)
        if producto.id in self.carro: 
            del self.carro[producto.id]
            self.guardarCarro()

    def restar(self, producto): 
        for key, value in self.carro.items(): 

            if key == str(producto.id): 
                value["cantidad"] = value["cantidad"] - 1

                if value["cantidad"] == 0: 
                    self.eliminar(producto)
                
                break

        self.guardarCarro()

    def limpiarCarro(self): 
        carro = self.session["carro"] = {}
        self.session.modifed = True