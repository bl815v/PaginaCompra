from logic.Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, volumen):
        super().__init__(nombre, precio)
        self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        self.volumen = volumen
