# -*-coding: utf-8 -*-
#!/usr/bin/env python
from RPi_AS3935 import RPi_AS3935
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM) #Inicia el GPIO
pin = 19 #Pin a usar para el IRQ
sensor = RPi_AS3935(address=0x03, bus=4) #Dirección del sensor
noise = 0
a = True
#----------Calibración----------#
sensor.reset() #Resetea el sensor
sensor.set_indoors(True) #Selección de interior o exterior
sensor.set_noise_floor(0) #Establece el nivel de ruido inicial
sensor.calibrate(tun_cap=0x09) #Número de capacitancia dividido entre 8
sensor.set_min_strikes(1) #Cantidad mínima de rayos para comenzar a sensar

#---------Archivo de escritura--------#
f = open("datos3.txt","a") #Apertura de archivo de datos
#---------Función de ajuste de Ruido------------#
def noise_calibration():
    global sensor,noise
    reason =sensor.get_interrupt()
    if reason == 0x01: #Ruido
        print ("Noise level too high - adjusting")
        sensor.raise_noise_floor() #ajusta el ruido elevando el voltaje
        noise = sensor.get_noise_floor() #se guarda nivel de ruido
        print (noise)

#---------Función de toma de datos----------#
def handle_interrupt(channel):
    global sensor
    nodetecta = True
    while nodetecta:
        time.sleep(0.001)
        try:
            reason = sensor.get_interrupt()
        except:
            reason = 0x08
        if reason == 0x08: #Descarga detectada
            now = datetime.now().strftime('%H:%M:%S.%f - %Y/%m/%d') #Tiempo actual UTC en str
            print ("¡Se ha detectado una descarga!")
            outstring = str(now)  + " " + str(0) + " " + str(0)
        #Cadena de escritura
            print (outstring)
            f.write("\n")
            f.write(outstring)
            nodetecta = False

GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pin,GPIO.RISING,callback=handle_interrupt)

try:
    print ("AS3935 Lightning Detection Monitor Scrip CMS - FIBUAP - v3.1")
    print ("Estado del Monitor: ONLINE")
    print ("")
    startTime = time.time()
    print ("Iniciando...")
    print ("Fecha de inicio(UTC): "+datetime.now().strftime('%H:%M:%S.%f -%Y/%m/%d'))
    print ("Ajustando ruido...")
#------------Ciclo de Ajuste de Ruido------------#    
    while a:
        noise_calibration() #Realiza la función
        endTime = time.time()
        totalTime = endTime - startTime
        if totalTime >= 10: #El sensor realiza el ajuste en aprox. 3 segundos se deja un margen de tiempo por cualquier cambio
            a = False #Una ves ajustado se sale del ciclo y comienza el modo de monitoreo
    print ("Ruido Ajustado")
#------------Modo de Monioreo------------------#    
    print ("Esperando una descarga")
    while True:
        sensor.reset() #Se reinicia el sensor para no guardar información de descargas pasadas.
        sensor.__init__(address=0x03, bus=4)
        sensor.set_noise_floor(noise) #Se ajusta el ruido al nivel del ciclo pasado
        sensor.set_min_strikes(1) #La toma de datos se hace a cada descarga
        sensor.calibrate(tun_cap=0x09) #Se vuelve a establecer el número de capacitacia debido al reinicio
        handle_interrupt(pin) #Se toman los datos y se guarda la información en el archivo de texto
except KeyboardInterrupt:
    print ("Estado del Monitor: OFFLINE")
    print ("Cantidad de descargas minimas: "+str(sensor.get_min_strikes()))
    print ("Nivel de ruido: "+str(noise))
    print ("")
finally:
    f.close()
    GPIO.cleanup()
