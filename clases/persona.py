class Persona: #definimos la clase, que es una receta para crear un objeto. la clase es una plantilla. las clases se ponen con mayúscula (indica que no es una función)
    edad = 0   #atributo/característica de la clase/objeto que vamos a crear
    nacionalidad = "paraguaya"
#cuando def está dentro de class es un método, cuando está fuera es una función
    def __init__ (self, un_nombre, una_altura, un_peso): #__init__ método constructor. métodos: funciones dentro una clase, opera para el objeto de adentro
        self.mi_nombre = un_nombre #usamos self para referirnos al objeto mismo
        self.altura = una_altura #al usar self. se asigna una variable al objeto
        self.peso = un_peso
        print("Hola naci, me llamo", self.mi_nombre) #mensaje que indica que se creó el objeto
 
    def cumple(self): #cumple es un método de la clase persona
        self.edad = self.edad + 1 #aumenta la propiedad edad en 1

    def asignar_edad (self, una_edad): #asignar_edad es un método que recibe un argumento numérico y asigna a la propiedad edad del objeto
        self.edad = una_edad
    
    def asignar_nacionalidad (self, una_nacionalidad):
        self.nacionalidad = una_nacionalidad

    def saludar (self):
        print("Hola soy",self.mi_nombre, "y mi nacionalidad es", self.nacionalidad)
    
    def imc (self):
        print((self.peso)/(self.altura**2))
    


pepe = Persona("Pepito", 1.61, 65) #pepe es el objeto de la clase persona
pepa = Persona("Pepita", 1.61, 69) #objeto pepa
print(pepe.edad) #imprime la edad asignada en la variable, o sea va a tener valor 0
print(pepe.mi_nombre) #imprime el nombre Pepito asignado con texto en el objeto pepe

print(pepe.nacionalidad)

pepe.asignar_nacionalidad("argentina")

print(pepe.nacionalidad)

pepe.cumple()
print(pepe.edad)

pepe.saludar()

pepa.saludar()

print(pepa.altura)
print(pepa.peso)

pepa.imc()