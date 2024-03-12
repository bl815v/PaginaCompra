
class Compra:
    def __init__(self, producto, cantidad, metodoPago):
        self.producto = producto
        self.cantidad = cantidad
        self.metodoPago = metodoPago

    def getProducto(self):
        return self.producto

    def setProducto(self, producto):
        self.producto = producto

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getMetodoPago(self):
        return self.metodoPago

    def setMetodoPago(self, metodoPago):
        self.metodoPago = metodoPago

