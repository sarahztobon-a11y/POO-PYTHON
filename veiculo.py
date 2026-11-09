
class Vehiculo:
  
    medio = "Transporte"

    
    def __init__(self, nombre, velocidad, motor, llantas):
        self.nombre = nombre
        self.velocidad = velocidad
        self.motor = motor
        self.llantas = llantas  

    
    def descripcion(self):
        return f"El {self.nombre} tiene un motor tipo '{self.motor}', una velocidad máxima de {self.velocidad} km/h y cantidad de llantas: {self.llantas}."


avion = Vehiculo("Avión", 900, "Turbofán", "Tiene tren de aterrizaje (varias llantas)")
helicoptero = Vehiculo("Helicóptero", 280, "Turboeje", "Tiene ruedas pequeñas")
moto = Vehiculo("Moto", 180, "Monocilíndrico de 4 tiempos", "2 llantas")
submarino = Vehiculo("Submarino", 45, "Nuclear", "No tiene llantas")
barco = Vehiculo("Barco", 50, "Diesel marino", "No tiene llantas")


print(avion.descripcion())
print(helicoptero.descripcion())
print(moto.descripcion())
print(submarino.descripcion())
print(barco.descripcion())