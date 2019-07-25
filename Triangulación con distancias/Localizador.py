def triangular() :

    import math
    import Fun
    import linecache

    # -----------------------------------------------------------------------------------------------
    #
    #                                   Triangulación
    #
    #
    # Este programa toma las coordenadas de 3 sensores, asi como las distancias medidas por ellos,
    # para obtener la ubicación del origen del evento.
    #
    # Pasos realizados:
    #  1- Lectura de datos
    #  2- Cálculo de coordenadas idealizado
    #  3- Cálculo de coordenadas reales
    #  4- Prueba de tolerancia
    #  5- Escritura de evento
    #
    # Condiciones para funcionamiento del programa:
    #  - No colocar un par de sensores tal que la recta que los une sea completamente vertical
    #  - No colocar los 3 sensores tal que una sola recta una a los 3
    #
    #                             x                            
    #                            /                    x
    #                           /                     |
    #  - Es decir, evitar:     x          ,           |
    #                         /                       |
    #                        /                        x
    #                       x
    #
    # La primera condición evita que exista doble solución, mientras que la segunda evita
    # problemas al calcular la pendiente. Alejarse de estos casos puede incrementar la
    # presición de los cálculos.
    #
    # Lee coordenadas y devuelve los datos de la forma (lat,lon).
    #
    # --------------------------------------------------------------------------------------------

    #---------- Lectura de datos inicial --------------------

    coordenadas = open('CoordenadasSensores.txt','r')

    distancias = open('Distancias123.txt','r')

    archivo = open('Ubicaciones.txt','w')

    b1, a1 = [float(x) for x in coordenadas.readline().split()]

    b2, a2 = [float(x) for x in coordenadas.readline().split()]

    b3, a3 = [float(x) for x in coordenadas.readline().split()]

    tolerancia = float(input("Inserte el radio de tolerancia en metros: " ))

    tolerancia = Fun.mTOgrad(tolerancia)

    line = distancias.readline()

    j = 1


    

    while line:
        # ------------ Lectura de datos continua------------

        r1, r2, r3 = [float(x) for x in line.split()]
    


        # ---- Cálculo de coordenadas idealizado -----------

        distancia12 = ((a2 - a1)**2 + (b2 - b1)**2)**(1/2)

        distancia13 = ((a3 - a1)**2 + (b3 - b1)**2)**(1/2)


        r1 = Fun.mTOgrad(r1)

        r2 = Fun.mTOgrad(r2)

        r3 = Fun.mTOgrad(r3)


        #print(distancia12, distancia13)

        #print(r1, r2, r3)
        

        x1, y1 = Fun.ideales(distancia12, r1, r2)

        x2, y2 = Fun.ideales(distancia13, r1, r3)





        # ------- Cálculo de coordenadas reales ------------

        e11, e21, e12, e22 = Fun.reales(a1, b1, a2, b2, x1, y1)


        e13, e23, e14, e24 = Fun.reales(a1, b1, a3, b3, x2, y2)
        



        # ------------ Prueba de tolerancia ----------------

        distanciaAB = ((e11 - e12)**2 + (e21 - e22)**2)**(1/2)

        distanciaAC = ((e11 - e13)**2 + (e21 - e23)**2)**(1/2)

        distanciaAD = ((e11 - e14)**2 + (e21 - e24)**2)**(1/2)

        distanciaBC = ((e12 - e13)**2 + (e22 - e23)**2)**(1/2)

        distanciaBD = ((e12 - e14)**2 + (e22 - e24)**2)**(1/2)

        distanciaCD = ((e13 - e14)**2 + (e23 - e24)**2)**(1/2)

        # Ordenamos las distancias de mayor a menor, para
        # obtener la distancia menor.

        orden = [distanciaAB,distanciaAC,distanciaAD,distanciaBC,distanciaBD,distanciaCD]
        
        i=0

        while (i <= 4):
            n=i+1
            while (n <= 5):
                if (orden[i] < orden[n]):
                    aux = orden[i]
                    orden[i] = orden[n]
                    orden[n] = aux

                n=n+1
                
            i=i+1


        # Hacemos la prueba de tolerancia con la distancia
        # menor, y escribimos el resultado si se cumple.

        if (orden[5] > tolerancia):
            
            print("El evento está fuera de rango o la presición deseada no se ha cumplido")

        elif (distanciaAB == orden[5]):

            e1 = (e11 + e12)/2

            e2 = (e21 + e22)/2

            print("El evento ",j," se encuentra en: (",e2,",",e1,")")

            archivo.write("[" + str(e2) + ", " + str(e1) + ", 'Evento " + str(j) + "']," + "\n")

        elif (distanciaAC == orden[5]):

            e1 = (e11 + e13)/2

            e2 = (e21 + e23)/2

            print("El evento ",j," se encuentra en: (",e2,",",e1,")")

            archivo.write("[" + str(e2) + ", " + str(e1) + ", 'Evento " + str(j) + "']," + "\n")

        elif (distanciaAD == orden[5]):

            e1 = (e11 + e14)/2

            e2 = (e21 + e24)/2

            print("El evento ",j," se encuentra en: (",e2,",",e1,")")

            archivo.write("[" + str(e2) + ", " + str(e1) + ", 'Evento " + str(j) + "']," + "\n")

        elif (distanciaBC == orden[5]):

            e1 = (e12 + e13)/2

            e2 = (e22 + e23)/2

            print("El evento ",j," se encuentra en: (",e2,",",e1,")")

            archivo.write("[" + str(e2) + ", " + str(e1) + ", 'Evento " + str(j) + "']," + "\n")

        elif (distanciaBD == orden[5]):

            e1 = (e12 + e14)/2

            e2 = (e22 + e24)/2

            print("El evento ",j," se encuentra en: (",e2,",",e1,")")

            archivo.write("[" + str(e2) + ", " + str(e1) + ", 'Evento " + str(j) + "']," + "\n")

        elif (distanciaCD == orden[5]):

            e1 = (e13 + e14)/2

            e2 = (e23 + e24)/2

            print("El evento ",j," se encuentra en: (",e2,",",e1,")")

            archivo.write("[" + str(e2) + ", " + str(e1) + ", 'Evento " + str(j) + "']," + "\n")


        line = distancias.readline()

        j = j + 1
        
        if not line:
            break

    archivo.close()
    coordenadas.close()
    distancias.close()




