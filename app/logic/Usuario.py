
class Usuario:
    def __init__(self, nombres, apellidos, email, celular, tipoDocumento, numDocumento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.celular = celular
        self.tipoDocumento = tipoDocumento
        self.numDocumento = numDocumento

    def getNombres(self):
        return self.nombres

    def setNombres(self, nombres):
        self.nombres = nombres

    def getApellidos(self):
        return self.apellidos

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getCelular(self):
        return self.celular

    def setCelular(self, celular):
        self.celular = celular

    def getTipoDocumento(self):
        return self.tipoDocumento

    def setTipoDocumento(self, tipoDocumento):
        self.tipoDocumento = tipoDocumento

    def getNumDocumento(self):
        return self.numDocumento

    def setNumDocumento(self, numDocumento):
        self.numDocumento = numDocumento
