#Repaso
"Liliana" #String/cadena de texto/str, siempre entre comillas
30 #Integer/Entero/int
[] #Lista vacía
["Liliana", 30] #Lista de dos elementos
#Variables: caja donde podes poner valores. El nombre tiene que ser significativo (Buenas Prácticas)
#A la Variable se le asigna un valor usando Es Igual. Ej Nombre = Liliana
nombre = "Liliana" #nombre significativo, sin espacio, sin signos (con excepción de guión bajo), sin acento
edad = 30 #número entero, puede contener una operación, Ej 10+20, no así "10+20"
datos = ["Liliana", 30] #dos elementos contenidos en una lista
print(datos[0], datos[1]) #acceder a un elemento de la lista
datos.append("Nutricionista") #agregar un elemento a la lista
print(datos) #imprime ['Liliana', 30, 'Nutricionista']
datos.pop() #eliminar el último elemento agregado a la lista
print(datos) ##imprime ['Liliana', 30]
#for recorre una lista, que tiene una variable que toma en cada vuelta
for x in datos: #todo lo que termine en : dentro de un for, forma un bloque de código
    print(datos) #el número de veces que repite depende de la cantidad de elementos contenidos en la lista
print(len(datos)) #mide la cantidad de elementos
for x in datos:
    print(datos)
#Para imprimir los números del 1 al 10
for x in range(1,11):
    print(x)

a = 0 #se le asigna un valor a suma para que exista la variable
for x in range(1,11): #1,2,3,4,5,6,7,8,9,10
    a = a + x  #0+1,1+2,3+3,6+4,10+5,15+6,21+7,28+8,36+9,45+10
print(a) #1+2+3+4+5+6+7+8+9+10=55
# for numero in range(1,10) #1,2,3,4,5,6,7,8,9,10

for numero in [1,2,3,4,5,6,7,8,9,10]: #1,2,3,4,5,6,7,8,9,10 sin escribir range, pero mencionando cada valor
    print(numero)

#Funciones
#def es la palabra designada que define una función
#def nombre_de_la_funcion(argumento/parámetro): # : tiene relación con un bloque de código
#crear una función resta, que reciba como parámetro dos números y retorne la resta de esos números
#luego llamar a la función e imprimir el resultado

def resta (num1, num2):
    return num1 - num2

resta(100,90)
print(resta(100,90))

def saludo (nombre, edad):
    print("Hola, soy", nombre, "y tengo", edad, "años")

saludo(nombre, edad)

listita = [1,2,3,4,5]
def suma_lista (listadenumeros):
    a = 0
    for numero in listadenumeros:
        a = a + numero
        print(a)
suma_lista(listita)

listota = [100,5,5]
def suma_lista (listadenumeros):
    b = 0
    for numero in listadenumeros:
        b = b + numero
        print(b)
suma_lista(listota)

listita = [1,4,9,16,25]
def lista_cuadrado (listadenumeros):
    for numero in listadenumeros:
        c = numero * numero
        print(c)
lista_cuadrado(listita)

cuadrados = [1,2,3,4,5]

def lista_cuadrado (numeros_elevados_al_cuadrado): #el nombre del parámetro es como una etiqueta
    d = [] #se crea un espacio, una lista vacía, donde van a ir los resultados
    e = 0 #se crea una variable que indique que ese es el elemento que va a ingresar a la lista vacía
    for f in cuadrados: #el for recorre la lista, la varible d es la que va a cambiar de valor
        e = f * f #acá se le da un valor a la variable que debe estar previamente creada, en cada ciclo cambia el valor
        d.append(e) #lo que se va a agregar es la multiplicación de la varible del for (d) y se le agrega e que = a d*d
    return d #qué es lo que queres que te devuelva la función

cuadrado_de_listas = lista_cuadrado(cuadrados)
print(cuadrado_de_listas)