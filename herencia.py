#Objetos. Herencia 1
class Vehiculos():
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True
        
    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):

        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):

    def carga(self, cargado):
        self.cargado=cargar
        if self.carga:
            return "La furgoneta está cargada"
        else:
            return "La furggonata no está cargada"


class Moto(Vehiculos):
    
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)



miMoto=Moto("Yamaha", "Tmax")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Trafic")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.cargado(True)