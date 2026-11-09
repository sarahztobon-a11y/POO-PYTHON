#tributos de clases: son caracteristicas comunes a todos los objetos de una clase
#se definen dentro de la clase pero fuera de cualquier metodo.
#se accede a ellos mediante la clase o mediante un objeto de clase.

class perro:
    #atributos de clase
    especie = "Canis familiaris"

#self: es una referencia al objeto que se esta creando o al objeto que esta llamando al metodo.

    #constructor: es un metodo especial que se ejecuta automaticamente al crear un objeto de la clase.
    def __init__(self, nombre, edad):
        #atributos de instancia: son caracteristicas propias de cada objeto de una clase
        self.nombre = nombre
        self.edad = edad


#esto es un metodo de instancia: es una funcion que pertenece a un objeto de una clase y puede acceder a sus atributos y metodos.
#siempre se usa con verbos infinitivos (ar, er, ir) y se define dentro de la clase.
    def ladrar(self):
        return f"{self.nombre} dice: ¡guau, guau!"

rex = perro("Rex", 3)
luna = perro("Luna", 5)
#uso de los objetos (instancias) de la clase perro


#acceso a los atributos de clase mediante la clase

print(f"especie de {rex.nombre}: {perro.especie}")
print(f"especie de {luna.nombre}: {perro.especie}")


#acceso a los atributos de instancia mediante el objeto
print(f"{rex.nombre} tiene {rex.edad} años.")
print(f"{luna.nombre} tiene {luna.edad} años.")

#llamada a los metodos de instancia mediante el objeto
print(rex.ladrar())
print(luna.ladrar())

