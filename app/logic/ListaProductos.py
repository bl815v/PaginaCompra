from logic.Producto import Producto
from logic.Galleta import Galleta
from logic.Bebida import Bebida

class ListaProductos:
    def __init__(self):
        self.productos = [
            Galleta("fresa", 1500),
            Galleta("chocolate", 1500),
            Producto("Almuerzo", 50000),
            Bebida("Cappuccino", 7500, "15oz")
        ]

    def getOpcionesProductos(self):
        opciones = []
        for producto in self.productos:
            opciones.append({"nombre": producto.getNombre(), "precio": producto.getPrecio()})
        return opciones