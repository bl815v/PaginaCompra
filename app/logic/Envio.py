
def verificarOpcion(opcion):
    if opcion == "on":
        opcion = "Si"
    else:
        opcion = "No"
    return opcion


class Envio:
    def __init__(self, ciudad, direccionEntrega, descripcion, propina, envioPrioritario):
        AuxPropina = verificarOpcion(propina)
        auxEnvioPrioritario = verificarOpcion(envioPrioritario)
        self.ciudad = ciudad
        self.direccionEntrega = direccionEntrega
        self.descripcion = descripcion
        self.propina = AuxPropina
        self.envioPrioritario = auxEnvioPrioritario


    def getCiudad(self):
        return self.ciudad

    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    def getDireccionEntrega(self):
        return self.direccionEntrega

    def setDireccionEntrega(self, direccionEntrega):
        self.direccionEntrega = direccionEntrega

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getPropina(self):
        return self.propina

    def setPropina(self, propina):
        self.propina = propina

    def getEnvioPrioritario(self):
        return self.envioPrioritario

    def setEnvioPrioritario(self, envioPrioritario):
        self.envioPrioritario = envioPrioritario
