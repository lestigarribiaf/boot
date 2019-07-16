#Repaso
ingr_pan = ["harina", "levadura", "sal", "azucar", "agua"]
def imprimir_lista(ingredientes):
    for producto in ingredientes:
        print(producto)
imprimir_lista(ingr_pan)

#Condicionales
#Forma en la que uno puede preguntarle algo a la compu, y saber si la respuesta es verdadera o falsa
#if es el operador de la pregunta
#else si no
#signo es igual en programación es de asignación, en el caso de que se trate de condición, se usa doble signo es igual ==
# == es igual
# > mayor que
# < menor que
# >= mayor o igual que (sin espacio)
# <= menor o igual que
# != distinto o no igual

necesidad_de_pimienta = 0.005

if necesidad_de_pimienta > 0.010:
    print("Sí, la cantidad necesaria de pimienta es mayor")
else:
    print("No, la cantidad necesaria de pimienta es menor")

if necesidad_de_pimienta > 0.001:
    print("Sí, la cantidad necesaria de pimienta es mayor")
else:
    print("No, la cantidad necesaria de pimienta es menor")

nota_alumno = 100
def nota (nota_60): #definir parámetro a ser analizado
    if nota_60 > 60: #se analiza el parámetro
        print("Aprobado")
    else:
        print("Aplazado")
nota(nota_alumno) #la función ya indica que tiene que imprimir al ser mencionado

a = 20
if a > 5 and a < 10: #hay que indicar para cada caso cuál es la variable, en este caso a, que se mencionó dos veces
    print("a es mayor a 5 y menor que 10")
else:
    print("a no está en el rango, alguna de las 2 condiciones no se cumplió")

a = 6
if a > 5:
    if a < 10:
        if a != 7:
            print("a es mayor a 5 y menor que 10 y distinto que 7")

a = 1
if a > 5 or a < 10:
    print("a es mayor que 5 o menor que 10")
else:
    print("a no es mayor que 5 ni menor que 10")

print(5==6)
print(5>3)
print(5!=4)
print(5!=5)

edad = 22
if edad > 18:
    print("Debería estar en la universidad")
elif edad > 13: #elif equivale a un "si no" y hace una pregunta nueva
    print("Debería estar en secundaria")
elif edad > 6:
    print("Debería estar en primaria")
else:
    print("Debería estar en su casa")

#Anidado
if edad > 18:
    print("universidad")
else:
    if edad > 13:
        print("secundaria")
    else:
        if edad > 6:
            print("primaria")
        else:
            print("bbdlc")

def calificacion (valor):
    if valor >= 0 and valor <= 100:
        if valor <= 60:
            print("Aplazado")
        elif valor <= 70:
            print("2")
        elif valor <= 80:
            print("3")
        elif valor <= 90:
            print("4")
        else:
            print("5")
    else:
        print("Nota fuera de rango")

#nombre = input("Ingresa tu nombre: ")
#print("Hola", nombre)
#todo lo que vaya dentro de un input, va como string

num1 = int(input("Ingresa el primer numero a sumar: "))
num2 = int(input("Ingresa el segundo numero a sumar: "))
print("El resultado es: ", num1 + num2)

#Pedir al usuario que ingrese tres números y multiplicarlos entre sí, imprimir el resultado

num1 = int(input("Ingresa el primer numero a multiplicar: "))
num2 = int(input("Ingresa el segundo numero a multiplicar: "))
num3 = int(input("Ingresa el tercer numero a multiplicar: "))
print("El resultado es: ", num1 * num2 * num3)

#Pedir al usuario un numero del 1 al 100 y llamar a la funcion que retornaba la nota que creamos hace un rato
#utilizando el valor ingresado por el usuario

puntaje = int(input("Ingresa un numero del 1 al 100: "))
print("Tu nota es: "), calificacion(puntaje)

#año bisiesto: divisible entre 4, no divisible entre 100

#Bucle while: Mientras
#en for se recorría un rango
#en while recorre hasta que se cumpla una condición

x = 0
while x != 5:
    print("Hola, esto es un bucle while, se va ejecutar mientras x sea igual a 5")
    x= int(input("Ingreso un número: "))
    print("El valor de x ahora es ", x)
print("Fin")

contador = 0
while contador < 10:
    print("Sigo en el bucle while")
    contador = contador + 1
    print("Se repitio", contador, "veces")

contador = 10
while contador > 0:
    print("Sigo en el bucle while")
    contador = contador - 1
    print("Te quedan", contador, "oportunidades")
print("Terminó")
'''
#Usando while pedir al usuario (input) ingredientes para hacer una pizza y agregar a una lista,
#al final imprimir la lista
#Hacer que se repita 5 veces algo
#Hacer que me pida un ingrediente en cada ciclo/repetición
#Hacer que se agregue a la lista
#Imprimir
'''
lista_ingredientes = [] #se crea una lista vacía
contador = 0 #iniciamos el contador en 0
while contador < 5: #se va a repetir 5 veces
    ingr = input("Ingrese un ingrediente: ") #se pide un dato
    lista_ingredientes.append(ingr) #agregamos el ingrediente a la lista
    contador = contador + 1 #aumenta el contador

print("Los ingredientes de la pizza son:", lista_ingredientes) #se imprime

ingredientes_pizza = []
print("Ingrese los ingredientes de la pizza")
while len(ingredientes_pizza) < 5:
    ing = input ("Ingrediente: ")
    ingredientes_pizza.append(ing)
print("La lista de ingredientes es: ", ingredientes_pizza)

numero_secreto = 7
adivino =  False

while adivino == False:
    apuesta = input("Adivina el número secreto del 1 al 10: ")

    if int(apuesta) == numero_secreto:
        print("Ganaste!")
        adivino = True
    else:
        print("Seguí participando")

numero_secreto = 15
adivino = False

while adivino == False:
    apuesta = input("Adivina el número secreto del 1 al 100: ")

    if int(apuesta) == numero_secreto:
        print("Ganaste!")
        adivino = True
    elif int(apuesta) < 100 and int(apuesta) >50:
        print("Ingresa un número menor: ")
    elif int(apuesta) < 50 and int(apuesta) >14:
        print("Ingresa un múltiplo de 5: ")
    else:
        print("Seguí participando")