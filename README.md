---------------------------------------------------------

A continuación se describen los detalles necesarios
para hacer funcionar la lectura, procesamiento
y visualización de datos que ofrece el programa.

Contenido:

	1- Red compartida
	
	2- Especificación de ubicación de los sensores
	
	3- Conexiones multiples y formato de lectura
	
	4- Uso del juntador
	
	5- Uso de Google Maps


--------------------------------------------------------


----------------- 1- Red Compartida --------------------

La red compartida es necesaria para que alguna computadora
pueda accesar los datos obtenidos por los 3 sensores. El objetivo
es obtener un directorio local que se actualice con los datos de
los 3 sensores, esto se puede conseguir de distintas formas,
incluyendo el uso de:

- Base de datos
- Repositorio Github (con uso de crontab)
- Servicio de sincronización de Dropbox




---- 2- Especificación de ubicación de los sensores ----

El calculo TDOA (Time Difference Of Arrival) requiere conocer
las coordenadas de los sensores. 

Estas se especifican en el archivo "CoordsSensores.txt", con el
formato "Latitud, Longitud", la línea 1 corresponde al sensor 1,
la 2 al sensor 2, asi mismo con el sensor 3. Estos pueden
obtenerse a través de Google Maps, añadiendo un pin en la ubicación
de estos muestra la información necesaria.

Un ejemplo ubicado en Puebla, PUE:

19.0163366 -98.2463520

18.9840362 -98.1768171

19.0694769 -98.2123514

Para multiples sensores en 1 ubicación, basta con especificar
las coordenadas en una línea, el par o terna de sensores será
considerado como 1, donde se limpian los casos de redundancia.

Para mejorar la precisión, los sensores deberán ser ubicados
idealmente a una distancia entre ellos desde 6 km hasta 20 km,
esto para el sensor AS3935. Además, evitar un arreglo donde una 
recta pueda unir los 3 puntos. Los datos con mayor precisión serán
de aquellos eventos que se encuentren dentro del triangulo formado
por los 3 sensores.

Para calcular la distancia ideal entre los sensores, se considera
que debe existir una diferencia considerable de llegada de la señal
entre estos, en el caso del AS3935 que cuenta con una precisión
de tiempo de 1 microsegundo, la velocidad de la luz es de 
299,792,458 m/s, para que exista una diferencia de llegada de 20
microsegundos (para precisión aceptable), es necesario que los 
sensores se encuentren a una distancia mínima de x = v*t = 6000 m.
La distancia máxima se restringe a 20 km ya que a distancias mayores
que esta la eficiencia se reduce considerblemente, para el AS3935.




---- 3- Conexiones multiples y formato de lectura ------

Para mejorar la eficiencia conectando múltiples sensores, o para 
conectar un sensor distinto al AS3935, se explica el formato con 
el que funciona el programa en caso de necesitar modificaciones.

El programa "ControlDavidn-m.py" toma los eventos registrados por
el sensor AS3935 número m en la ubicación n y los guarda en 
"datosn.txt". El sensor utiliza el protocolo I2C y ocupa la 
dirección 0x03 en el bus 1, el IRQ, donde se toman los datos, son
obtenidos desde un pin seleccionado del GPIO de la Raspberry PI.

Por decreto, el sensor 1 utiliza el pin 17, el 2 utiliza el 16,
y el 3 utiliza el 19. Estos pueden ser cambiados desde el código.
La Raspberry PI puede conectar múltiples sensores I2C agregando
bus adicionales, esto se consigue con los siguientes comandos
de la terminal:

cd /boot

sudo nano config.txt

En el archivo de texto, en la sección donde se activa SPI e I2C,
se agrega la siguiente línea para conectar el sensor 2:

dtoverlay=i2c-gpio,bus=4,i2c_gpio_delay_us=1,i2c_gpio_sda=20,i2c_gpio_scl=21

Donde se utiliza el pin 20 como SDA y el pin 21 como SCL, esto
puede cambiarse si es necesario. El sensor 2 ahora se comunica en
el bus 3. Para agregar el sensor 3, se agrega la línea:

dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=1,i2c_gpio_sda=5,i2c_gpio_scl=6

Donde se utiliza el pin 5 como SDA y el pin 6 como SCL, esto
puede cambiarse si es necesario. El sensor 3 ahora se comunica en
el bus 4.

Reiniciar la Rasberry PI después de realizar los cambios, y asegurar
que I2C se encuentre activado, hace posible conectar hasta 3 sensores
en una Rasberry PI. Este procedimiento se realiza cuando tienen la
misma dirección, en este caso, 0x03.

En caso de utilizar otro sensor, se deberá usar el programa
controlador que corresponda a este, sin embargo, para que el Juntador
lea los datos correctamente, será necesario sean guardados en un
archivo con el nombre "datosn.txt", con el formato:

tiempo - fecha distancia energia

Donde el tiempo tiene formato: Hrs:Min:Seg
Fecha tiene el formato: Año/Mes/Día
Distancia y energía son despreciados

Un ejemplo:

19:43:55.447913 - 2018/10/05 1 61480




------------------ 4- Uso del Juntador -----------------

El programa "Juntador.py" realiza el proceso de seleccionar un 
intervalo de tiempo para los datos, limpieza de datos en caso 
de tener registro múltiple de un solo evento, detección de 
eventos, y el cálculo TDOA para dar como salida las ubicaciones 
de los eventos en el formato adecuado para Google Maps. 

Al iniciar el programa, se especifica la fecha inicial y final
de los datos que se desean analizar, además, pide introducir
la tolerancia de tiempo para detección de eventos, es decir, la
diferencia de tiempo máxima para la detección de un evento entre
sensores, esto puede ser calculado con el método utilizado para
encontrar la distancia ideal entre los sensores.

El cálculo del TDOA utiliza paquetes de numpy y scipy de python 3.7.

Al terminar, se guardan las ubicaciones en 2 archivos,
"Ubicaciones.txt" contiene el formato adecuado para Google Maps,
mientras que "Ubitemps.txt" contiene mayor información sobre
el tiempo del evento.




----------------- 5- Uso de Google Maps ----------------

El programa "mapas.html" toma los eventos registrados por el
juntador y realiza una visualización de estos en Google Maps.

La utilización de Google Maps requiere una clave de desarrollador,
que se introduce en "mapas.html" en 'mapsApiKey'. Para obtenerla,
visite:

https://developers.google.com/maps/documentation/javascript/get-api-key

Para introducir los eventos que se desean visualizar, se copia
en el portapapeles los datos de "Ubicaciones.txt" y se pegan
en "mapas.html", debajo la línea con el comentario " //Sustituir 
datos en las líneas siguientes --------------------". Un ejemplo:

[18.999033645315656, -98.20617035993159, 'Evento 1'],

[19.032127165986186, -98.16968205226381, 'Evento 2'],

[19.05442562984624, -98.27344676176052, 'Evento 3']

Para visualizar los datos introducidos, el html se abre en un
navegador, preferentemente Google Chrome, Mozilla Firefox o
Chromium.

--------------------------------------------------------

Para mayor información y guias, consultar el archivo "referencias de
triangulación", "githubsync", y el datasheet del sensor.
