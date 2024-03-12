from logic.Producto import Producto

class Galleta(Producto):
    def __init__(self, sabor, precio):
        nombre = "Galleta de " + sabor
        super().__init__(nombre, precio)
        self.sabor = sabor

    def getSabor(self):
        return self.sabor

    def setSabor(self, sabor):
        self.sabor = sabor