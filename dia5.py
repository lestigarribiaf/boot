import RPi.GPIO as gpio #libreria para puertos
from time import sleep #para dar pausas

led_r = 23  #definimos los pines de GPI0 a utilizar
led_y = 24 
led_g = 25 

gpio.setmode(gpio.BCM) #modo BCM de la raspberry pi (broadcom soc channel)
gpio.setmode(led_r, gpio, OUT) #configuramos los puertos conectados a los leds como salida

while True: #bucle infinito
    gpio.output(led_r, True) #encendemos el led_r
    sleep(1) #pausa de un segundo
    gpio.output(led1, False) #apagamos el led_r
    sleep(1) #pausa de un segundo

#Este programa finaliza cuando hay una interrupción por teclado

#ejercicio:
#hacer que los tres leds parpadeen juntos con un intérvalo de 0.5 segundos

import RPi.GPIO as gpio #libreria para puertos
from time import sleep #para dar pausas

led_r = 23
led_y = 24
led_g = 25

gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)

while True:
	gpio.output(led_r,True) #encender
	gpio.output(led_g,True)
	gpio.output(led_y,True)
	sleep(0.5)
	gpio.output(led_r,False) #apagar
	gpio.output(led_g,False)
	gpio.output(led_y,False)
	sleep(0.5)

tiempo = 0.5
while True:
	gpio.output(led_r,True) #encender
	gpio.output(led_g,True)
	gpio.output(led_y,True)
	sleep(tiempo)
	gpio.output(led_r,False) #apagar
	gpio.output(led_g,False)
	gpio.output(led_y,False)
	sleep(tiempo0.5)

listaopen = [led_r, led_y, led_g]
while True:
	for x in listaopen:
		gpio.output(x, True)
		sleep(0.2)
		gpio.output(x, False)
		sleep(0.2)