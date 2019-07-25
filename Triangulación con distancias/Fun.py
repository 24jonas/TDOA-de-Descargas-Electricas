# -----------------------------------------------------------------------
#
#                            Modulo de funciones
#
"""
    Este modulo contiene las funciones que se utilizan en el programa
    localizador.
"""
#
#------------------------------------------------------------------------

import math


# Cálculo de coords ideales

def ideales(distancia, radio1, radio2) :
    """
       Devuelve (x,+-y) de el evento con ubicaciones de los sensores
       idealizadas.
    """

    x = (distancia**2 - radio2**2 + radio1**2)/(2*distancia)

    y = (((-distancia +radio2 -radio1)*(-distancia -radio2 +radio1)*(-distancia +radio2 +radio1)*(distancia +radio2 +radio1))**(1/2))/(2*distancia) 

    return x, y




# Cálculo de coords reales

def reales(a1, b1, a2, b2, x, y) :
    """
       Devuelve latitud y longitud de el evento (2 soluciones), según las
       coordenadas de los sensores (a,b) y la ubicación idealizada (x,y).
    """

    # La pendiente m
    m = (b2 - b1)/(a2 - a1)

    # Calculamos las coordenadas del punto C=(c1,c2), aquel que se encuentra
    # a una distancia x del sensor 1 y se encuentra sobre la línea que une a
    # los 2 sensores.

    c1 = a1 + x*math.cos(math.atan(m))

    c2 = m*(c1 - a1) + b1

    # Con la información del punto C, calculamos las coordenadas reales
    # como el punto E=(e1,e2).

    e21 = c2 + y*math.cos(math.atan(m))

    e22 = c2 - y*math.cos(math.atan(m))

    e11 = -m*e21 + c1 + m*c2

    e12 = -m*e22 + c1 + m*c2

    return e11, e21, e12, e22




# Conversión de dif. de grados a metros

def gradTOm(distanciaGRAD) :
    """
       Cambia la unidad de distancia calculada entre 2 puntos
       de grados a metros.
    """

    # Consideramos la tierra como una esfera

    radioterrestre = 6370000

    perimetro = 2*math.pi*radioterrestre

    distanciaM = (distanciaGRAD/360)*perimetro

    return distanciaM




# Conversión de metros a dif. de grados

def mTOgrad(distanciaM) :
    """
       Cambia la unidad de distancia calculada entre 2 puntos
       de metros a grados.
    """

    # Consideramos la tierra como una esfera

    radioterrestre = 6370000

    perimetro = 2*math.pi*radioterrestre

    distanciaGRAD = (distanciaM/perimetro)*360

    return distanciaGRAD
    


    


    

    
