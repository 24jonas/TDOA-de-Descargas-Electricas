# -----------------------------------------------------------------------------------------------------
#
#                                             Juntador
#
#
# Este programa toma los datos registrados por 3 sensores, el tiempo en que se mide un evento
# específicamente, para calcular las coordenadas de este, además, verifica que el mismo evento
# detectado por todos los sensores. El programa lee y entrega coordemadas (lat,lon), formato
# que maneja google maps.
#
# Pasos realizados:
#  1- Lectura de datos y limitadores
#  2- Acondicionamiento de datos
#  3- Busqueda de evento
#  4- Cálculo y registro de ubicaciones
#
#
# Se obtiene mejor precisión si los eventos se encuentran dentro del área inscrita por los sensores.
#
#
# -----------------------------------------------------------------------------------------------------




# --------------------- Lectura de datos y limitadores ------------------------------
import math

nologica = True

while nologica:
    
    nologica = False

    print("Inserte el tiempo inicial para analizar datos:")
    
    añoi = int(input("Año: " ))
    mesi = int(input("Mes: " ))
    diai = int(input("Día: " ))
    horai = int(input("Hora (24 horas): " ))
    
    print(" ")
    print("Inserte el tiempo final para analizar datos:")
    
    añof = int(input("Año: " ))
    mesf = int(input("Mes: " ))
    diaf = int(input("Día: " ))
    horaf = int(input("Hora (24 horas): " ))
    
    datos1 = open('datos1.txt','r')
    datos2 = open('datos2.txt','r')
    datos3 = open('datos3.txt','r')
    datos1sel = open('datos1sel.txt','w')
    datos2sel = open('datos2sel.txt','w')
    datos3sel = open('datos3sel.txt','w')
    
    print(" ")
    print("Inserte la tolerancia en segundos para detectar un evento (40us para dist. de sensores de 10km)")
    tole = float(input())
    print(" ")
    
    if (añoi > añof) or (horai < 0) or (horai > 24) or (horaf < 0) or (horaf > 24) or (mesi < 1) or (mesi > 12) or (mesf < 1) or (mesf > 31) or (diai < 1) or (diai > 31) or (diaf < 1) or (diaf > 31) or (añoi < 0) or (añof < 0) or (tole <= 0):
        nologica = True
        print("Existe un error en los datos especificados, porfavor verifique lo siguiente:")
        print(" -Fecha final sea después que fecha inicial")
        print(" -La hora sea en formato de 24 hrs")
        print(" -El día se encuentre entre 1 y 31")
        print(" -El mes se encuentre entre 1 y 12")
        print(" -La tolerancia sea un número real positivo")
        print(" ")




# -------------------- Acondicionamiento de datos ------------------------------------

line = datos1.readline()

while line:
    tiempo, raya, fecha, km, energia = line.split()
    año, mes, dia = fecha.split("/")
    hora, minuto, segundo = tiempo.split(":")
    
    if (int(hora) >= horai - abs(int(dia) - diai)*24 - abs(int(mes) - mesi)*744 - abs(int(año) - añoi)*271560) :
        if (int(dia) >= diai - abs(int(mes) - mesi)*31 - abs(int(año) - añoi)*365) :
            if (int(mes) >= mesi - abs(int(año) - añoi)*12) :
              if (int(año) >= añoi) :
                  if (int(año) <= añof) :
                        if (int(mes) <= mesf + abs(añof - int(año))*12) :
                            if (int(dia) <= diaf + abs(mesf - int(mes))*31 + abs(añof - int(año))*365) :
                                if (int(hora) <= horaf + abs(diaf - int(dia))*24 + abs(mesf - int(mes))*744 + abs(añof - int(año))*271560) :
                                    datos1sel.write(str(int(año)) + " " + str(int(mes)) + " " + str(int(dia)) + " " + str(int(hora)) + " " + str(float(minuto)*60 + float(segundo)) + "\n")
                                    

    line = datos1.readline()

datos1.close()
datos1sel.close()



line = datos2.readline()

while line:
    tiempo, raya, fecha, km, energia = line.split()
    año, mes, dia = fecha.split("/")
    hora, minuto, segundo = tiempo.split(":")
    
    if (int(hora) >= horai - abs(int(dia) - diai)*24 - abs(int(mes) - mesi)*744 - abs(int(año) - añoi)*271560) :
        if (int(dia) >= diai - abs(int(mes) - mesi)*31 - abs(int(año) - añoi)*365) :
            if (int(mes) >= mesi - abs(int(año) - añoi)*12) :
              if (int(año) >= añoi) :
                  if (int(año) <= añof) :
                        if (int(mes) <= mesf + abs(añof - int(año))*12) :
                            if (int(dia) <= diaf + abs(mesf - int(mes))*31 + abs(añof - int(año))*365) :
                                if (int(hora) <= horaf + abs(diaf - int(dia))*24 + abs(mesf - int(mes))*744 + abs(añof - int(año))*271560) :
                                    datos2sel.write(str(int(año)) + " " + str(int(mes)) + " " + str(int(dia)) + " " + str(int(hora)) + " " + str(float(minuto)*60 + float(segundo)) + "\n")
                                    

    line = datos2.readline()

datos2.close()
datos2sel.close()



line = datos3.readline()

while line:
    tiempo, raya, fecha, km, energia = line.split()
    año, mes, dia = fecha.split("/")
    hora, minuto, segundo = tiempo.split(":")
    
    if (int(hora) >= horai - abs(int(dia) - diai)*24 - abs(int(mes) - mesi)*744 - abs(int(año) - añoi)*271560) :
        if (int(dia) >= diai - abs(int(mes) - mesi)*31 - abs(int(año) - añoi)*365) :
            if (int(mes) >= mesi - abs(int(año) - añoi)*12) :
              if (int(año) >= añoi) :
                  if (int(año) <= añof) :
                        if (int(mes) <= mesf + abs(añof - int(año))*12) :
                            if (int(dia) <= diaf + abs(mesf - int(mes))*31 + abs(añof - int(año))*365) :
                                if (int(hora) <= horaf + abs(diaf - int(dia))*24 + abs(mesf - int(mes))*744 + abs(añof - int(año))*271560) :
                                    datos3sel.write(str(int(año)) + " " + str(int(mes)) + " " + str(int(dia)) + " " + str(int(hora)) + " " + str(float(minuto)*60 + float(segundo)) + "\n")
                                    

    line = datos3.readline()

datos3.close()
datos3sel.close()




# ---------------------- Detección de eventos -------------------------------


# Limpieza en caso de que el mismo evento sea detectado por un par

fn = 'datos1sel.txt'
arc = open(fn,"r")
line1 = arc.readline()
año1, mes1, dia1, hora1, minseg1 = line1.split()
line2 = arc.readline()
año2, mes2, dia2, hora2, minseg2 = line2.split()

while line2:
    año2, mes2, dia2, hora2, minseg2 = line2.split()
    if (año1 == año2) and (mes1 == mes2) and (dia1 == dia2) and (hora1 == hora2) and (abs(float(minseg1)-float(minseg2)) <= tole):
        f = open(fn)
        output = []
        for line in f:
            if str(line1) != line.strip():
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()
    line1 = line2
    año1, mes1, dia1, hora1, minseg1 = line1.split()
    line2 = arc.readline()
arc.close()

fn = 'datos2sel.txt'
arc = open(fn,"r")
line1 = arc.readline()
año1, mes1, dia1, hora1, minseg1 = line1.split()
line2 = arc.readline()
año2, mes2, dia2, hora2, minseg2 = line2.split()

while line2:
    año2, mes2, dia2, hora2, minseg2 = line2.split()
    if (año1 == año2) and (mes1 == mes2) and (dia1 == dia2) and (hora1 == hora2) and (abs(float(minseg1)-float(minseg2)) <= tole):
        f = open(fn)
        output = []
        for line in f:
            if str(line1) != line.strip():
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()
    line1 = line2
    año1, mes1, dia1, hora1, minseg1 = line1.split()
    line2 = arc.readline()
arc.close()


fn = 'datos3sel.txt'
arc = open(fn,"r")
line1 = arc.readline()
año1, mes1, dia1, hora1, minseg1 = line1.split()
line2 = arc.readline()
año2, mes2, dia2, hora2, minseg2 = line2.split()

while line2:
    año2, mes2, dia2, hora2, minseg2 = line2.split()
    if (año1 == año2) and (mes1 == mes2) and (dia1 == dia2) and (hora1 == hora2) and (abs(float(minseg1)-float(minseg2)) <= tole):
        f = open(fn)
        output = []
        for line in f:
            if str(line1) != line.strip():
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()
    line1 = line2
    año1, mes1, dia1, hora1, minseg1 = line1.split()
    line2 = arc.readline()
arc.close()




# Detección

d1sel = open('datos1sel.txt','r')
d2sel = open('datos2sel.txt','r')
d3sel = open('datos3sel.txt','r')
temp = open('tiempos123.txt','w')

line1 = d1sel.readline()
line2 = d2sel.readline()
line3 = d3sel.readline()

año, mes, dia, hora1, minseg1 = line1.split()
año, mes, dia, hora2, minseg2 = line2.split()
año, mes, dia, hora3, minseg3 = line3.split()
    
while line1:
    
    while int(hora2) == int(hora1) and line2:
        
        while int(hora3) == int(hora1) and line3:
            
            if (abs(float(minseg1) - float(minseg2)) <= tole) and (abs(float(minseg1) - float(minseg3)) <= tole) and (abs(float(minseg2) - float(minseg3)) <= tole):
               temp.write(str(minseg1) + " " + str(minseg2) + " " + str(minseg3) + " " + str(int(año)) + " " + str(int(mes)) + " " + str(int(dia)) + " " + str(int(hora1)) + " " + str(int(math.floor(float(minseg1)/60))) + "\n")
               
            line3 = d3sel.readline()
            if not line3:
                break
            año, mes, dia, hora3, minseg3 = line3.split()
            
        d3sel.close()
        d3sel = open('datos3sel.txt','r')
        line3 = d3sel.readline()
        año, mes, dia, hora3, minseg3 = line3.split()
        
        while int(hora3) < int(hora1):
            año, mes, dia, hora3, minseg3 = d3sel.readline().split() 
       
        line2 = d2sel.readline()
        if not line2:
            break
        año, mes, dia, hora2, minseg2 = line2.split()

    d2sel.close()
    d2sel = open('datos2sel.txt','r')
    line2 = d2sel.readline()
    año, mes, dia, hora2, minseg2 = line2.split()
    
    line1 = d1sel.readline()
    if not line1:
        break
    año, mes, dia, hora1, minseg1 = line1.split()
    
    while int(hora2) < int(hora1):
        año, mes, dia, hora2, minseg2 = d2sel.readline().split()
        
    while int(hora3) < int(hora1):
        año, mes, dia, hora3, minseg3 = d3sel.readline().split()
    
    


temp.close()

d1sel.close()
d2sel.close()
d3sel.close()




# ----------------- Cálculo y registro de ubicaciones -----------------------

coords = open('CoordsSensores.txt','r')
b1, a1 = [float(x) for x in coords.readline().split()]
b2, a2 = [float(x) for x in coords.readline().split()]
b3, a3 = [float(x) for x in coords.readline().split()]
coords.close()

centro_x = (a1 + a2 + a3)/3
centro_y = (b1 + b2 + b3)/3

c_ang = 299792458/111177.4734

archivo = open('Ubicaciones.txt','w')
archivo2 = open('Ubitemps.txt','w')
tiempos = open('tiempos123.txt','r')

j=1
line = tiempos.readline()

from math import sqrt
import numpy as np
from scipy.optimize import fsolve

def f(x):
    global D_ad
    global D_bd
    global D_cd
    
    global a1
    global b1
    
    global a2
    global b2
    
    global a3
    global b3
     
    y = np.zeros(2)
    
    if (D_ad >= D_bd) and (D_cd >= D_ad) :
        y[0] = sqrt((x[0]-a1)**2 + (x[1]-b1)**2) - sqrt((x[0]-a2)**2 + (x[1]-b2)**2) - (D_ad - D_bd)
        y[1] = sqrt((x[0]-a3)**2 + (x[1]-b3)**2) - sqrt((x[0]-a1)**2 + (x[1]-b1)**2) - (D_cd - D_ad)
    elif (D_ad <= D_bd) and (D_cd >= D_ad) :
        y[0] = - sqrt((x[0]-a1)**2 + (x[1]-b1)**2) + sqrt((x[0]-a2)**2 + (x[1]-b2)**2) - (- D_ad + D_bd)
        y[1] = sqrt((x[0]-a3)**2 + (x[1]-b3)**2) - sqrt((x[0]-a1)**2 + (x[1]-b1)**2) - (D_cd - D_ad)
    elif (D_ad >= D_bd) and (D_cd <= D_ad) :
        y[0] = sqrt((x[0]-a1)**2 + (x[1]-b1)**2) - sqrt((x[0]-a2)**2 + (x[1]-b2)**2) - (D_ad - D_bd)
        y[1] = - sqrt((x[0]-a3)**2 + (x[1]-b3)**2) + sqrt((x[0]-a1)**2 + (x[1]-b1)**2) - (- D_cd + D_ad)
    elif (D_ad <= D_bd) and (D_cd <= D_ad) :
        y[0] = - sqrt((x[0]-a1)**2 + (x[1]-b1)**2) + sqrt((x[0]-a2)**2 + (x[1]-b2)**2) - (- D_ad + D_bd)
        y[1] = - sqrt((x[0]-a3)**2 + (x[1]-b3)**2) + sqrt((x[0]-a1)**2 + (x[1]-b1)**2) - (- D_cd + D_ad)       
    return y

import warnings
warnings.simplefilter("error", RuntimeWarning)

while line:
    t_ad, t_bd, t_cd, año, mes, dia, hora, minuto = [float(x) for x in line.split()]
    
    D_ad = t_ad*c_ang
    D_bd = t_bd*c_ang
    D_cd = t_cd*c_ang
    
    x0 = np.array([centro_x,centro_y])
    
    try:    
        solution = fsolve(f, x0)
        archivo.write("[" + str(solution[1]) + ", " + str(solution[0]) + ", 'Evento " + str(j) + "']," + "\n")
        archivo2.write(str(solution[1]) + " " + str(solution[0]) + " " + str(j) + " " + str(int(año)) + " " + str(int(mes)) + " " + str(int(dia)) + " " + str(int(hora)) + " " + str(int(minuto)) + "\n")
        print("El evento ",j,"(","Año",int(año),"Mes",int(mes),"Día",int(dia),",",int(hora),"Hrs",int(minuto),"mins ), se encuentra en: (" + str(solution[1]) + ", " + str(solution[0]) + ")")
    except RuntimeWarning:
        print(" ")
        print("El evento",j,"se encuentra fuera del rango de precisión, intente cambiar variable centro")
        print(" ")
    
    
    
    
    j=j+1
    line = tiempos.readline()
    
tiempos.close()
archivo.close()
archivo2.close()

print(" ")
print("Los datos para graficar fueron guardados en Ubicaciones.txt")
print("Los datos con fecha fueron guardados en Ubitemps.txt, formato: lat, lon, evento, año, mes, dia, hora, minuto")
