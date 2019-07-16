print(2+2)

print(2*3)
print(12-2)
print(12/2)
print("Hola Mundo!") #saludo para iniciarse en programación
print("Liliana María Teresa") #string es una cadena de texto, el texto siempre está entre comillas
print("Liliana " * 10)
a = 2 #operador de asignación, se puede asignar valores variables
b = 4 #operador de asignación
print(a+b)
b = a + 6
print(a+b)
print(a, b) #la coma separa elementos
print("Las variables a y b equivalen respectivamente a los valores", a, b)
nombre = "Liliana," #texto siempre entre comillas, inclusive al asignar una variable
edad = 30
print("Hola, me llamo", nombre, "y tengo", edad, "años")
hobbies = "leer, dibujar y pintar." #texto siempre entre comillas, inclusive al asignar una variable
print("Hola! Me llamo", nombre,"tengo", edad, "años y mis hobbies son", hobbies,)
#el corchete siempre se refiere a una lista, las posiciones de una lista empiezan en 0 (cero)
datos = ["Liliana", 30]
datos[1] = 30
print("Hola! Me llamo", datos[0], "y tengo", datos[1], "años.")
datos.append #.append te permite agregar elementos a una lista
datos.append("Nutricionista")
print(datos)
print(datos[2])
datos.append("leer")
print(datos)
print(datos[3])
print("Hola! Me llamo", datos[0], "tengo", datos[1], "años", "soy", datos[2], "y me gusta", datos[3])
datos.pop() #al agregar .pop() se elimina el último elemento de la última lista
print(datos)
datos.append("pintar")
print("Hola! Me llamo", datos[0], "tengo", datos[1], "años", "soy", datos[2], "y me gusta", datos[3])
#función len() viene de lenght, y sirve para saber cuántos elementos tiene una lista
print(len(datos)) #imprimir la cantidad de elementos que tiene una lista
dimension_de_datos = len(datos) #en nombre de variables no se usan espacios ni puntos
print(datos)
print(dimension_de_datos)
datos.pop()
print(datos)
print(len(datos))
datos.append("dibujar y pintar")
print(datos)
print("Hola! Me llamo", datos[0], "tengo", datos[1], "años", "soy", datos[2], "y me gusta", datos[3])
print(len(datos))
print(dimension_de_datos)
print("La lista datos tiene", len(datos), "elementos")
print("La lista datos tiene", dimension_de_datos, "elementos")
numeros = [1,2,3,4,2,4,5,6,6,4,3,4,6,7,8,9,9,0,7,5,5,4,3,3,5,6,7,7,6,6,5,5,5,4,4,4,4,4,1,2,3,4,2,4,5,6,6,4,3,4,6,7,8,9,9,0,7,5,5,4,3,3,5,6,7,7,6,6,5,5,5,4,4,4,3,6]
print(len(numeros))
print(numeros[75])
print(len(numeros)-1)
print(numeros[75])
numeros = [1,2,3,4,2,4,5,6,6,4,3,4,6,7,8,9,9,0,7,5,5,4,3,3,5,6,7]
print(len(numeros))
print(len(numeros)-1)
print(numeros[26])
ultimo_numero = len(numeros) - 1
print(numeros[ultimo_numero])
#bucles/loops/ciclos/iteraciones/repetición
lista_temas = ["variables", "listas", "tipos de datos"]
#for = para
for concepto in lista_temas: #cuando hay dos puntos, lo que viene después es un bloque de código
#no importa el nombre de la variable del for, es temporal (ejemplo: concepto, en este caso)
    print("Hoy aprendí", concepto) #concepto va a tomar el elemento
    print("Qué gusto!") #bloque de código identados
print("Esto es lo que aprendí hoy") #no está en el bloque de código ya que ya la línea ya no está tabulada
#errores de identación: aparecen cuando se esperaban tabulaciones y no están, o cuando aparecieron tabulaciones que sobran
#la expresión "recorrer" se refiere a "for"
lista_temas = ["variables", "listas", "tipos de datos"]
for concepto in lista_temas:
    print("Hoy aprendí", concepto, "!!!")
print("FIN!!! :)")
for x in range(2):
    print("Liliana", x)
#acumulador
suma = 0
for x in range(1,11): #recursividad: se vuelve a usar una misma variable. 1+2+3+4+5+6+7+8+9+10=55
    suma = x + suma
print(suma)