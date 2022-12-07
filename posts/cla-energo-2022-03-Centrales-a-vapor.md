---
title: 03 Centrales a vapor
slug: cla-energo-2022-03-centrales-a-vapor
date: 2022-12-05
tags: 
category: energo
link: 
description: 
type: text
has_math: true
hidetitle: true
template: postb.tmpl
---

Centrales a vapor
=================

# Centrales térmicas en general
------------------------------------

![](/images/centrales-termicas.drawio.svg)

----
- La energía de los combustibles se transforma, calderas, camaras de combustión, etc. en energía térmica que se almacena en forma de vapor o gases
- Este vapor se convierte energía mecánica en una turbina o motor
- La energía mecánica se entrega a un generador eléctrico.

Toda central térmica consta de las siguientes partes

1. Entrada y abastecimiento de combustible
2. Instalación y provisión de agua para refrigeración y bombeo
3. Calderas y tratamiento de gases de combustión
4. Sala de máquinas con turbinas, motores, etc.
5. Sala de celdas y tableros de protección, medición, interruptores, etc.
6. Estación de transformación para transportar la energía.

El circuito de trabajo de una central térmica de vapor ronda el 40%. Podemos encontrar centrales que operan con diferentes combustibles primarios tales como:

1. Carbón
2. Fuel Oil
3. Gas Natural

# Circuito de combustible

## Centrales a carbón

- El costo de traslado es importante
    - cerca de puertos
    - ferrocarriles
- Se filtra el carbón
- Se almacena en tolvas
- Se lleva a torre central
- Mezclador: cenizas vs material (poder calorífico requerido)
- Molino: para enviar a los quemadores material más homogéneo
- Ventiladores tiro forzado: llevan el carbón a los quemadores con aire precalentado con gases de escape de la caldera
- Tubos agua-vapor (en paredes del hogar): se calientan con la caldera (hogar)
- En su salida hacia la atmósfera el aire de combustión se usa para calentar más el de agua de la caldera y los precalentadores de aire.
- Finalmente pasa por un ventilador de tiro forzado al separador de cenizas y la a chimenea para su expulsión final.

### pulverización

- **individual** Grupos de quemadores con sus propios molinos
- **centralizada** Un molino grande que distribuye a cada grupo de quemadores

El costo de quemadores y pulverizadores respresenta el 6-7% del costo total de la central.

## Centrales a Fuel Oil

- El costo de transporte es menor que el del carbón, el combustible es barato y se puede alimentar por camiones. (más flexible en su ubicación)
- Se almacena en una cisterna subterránea de hormigón y por medio de bombas se lo lleva a tanque de almacenamiento previo paso por filtros, o directamente a los tanques de uso diario
- Se lo debe mantener por encima de 90 C debido a su viscocidad por lo que tanto los camiones que transportan como la central debe estar aislada y caletanda en todas sus instalaciones para tal fin.
- Los tanques estan rodeados por un perímetro de mampostería para evitar desbordes en caso de rotura de un tanque.
- Para iniciar la combustión en la caldera se usa algún otro combustible mas fluido y liviano
- Dada la viscocidad del combustible las bombas son del tipo tornillo sin fin

## Centrales  a gas natural

Las centrales a gas también pueden quemar fuel-oil para permitir que siguan funcionando ante una interrupción del gasoducto (por imposibilidad de almacenar el gas).
El circuito es sencillo y económico: 

- A la entrada de la planta se ubican regualdores de presión para alimentar a los quemadores con gas a la presión adecauada para su correcto funcionamiento (25 a 2 kg/cm^2). 
- El caudal se regula con una válvula ubicada antes de los quemadores
- Tiene ventajas respecto a los otros combustibles no renovables: mejor rendimiento, menor contaminación, etc. pero compite con el uso domiciliario e industrial del mismo 

#3 Regulación de la combustión

Para entregar una potencia determinada, cada caldera utiliza
- una cantidad de combustible
- un volumen de aire de combustión
- un volumnen de gases de combustión a extraer 
- un volumen de agua para alimentar la caldera

Esta regulación se debe hacer en forma automática (a excepción de arranques y paradas)

Si el generador disminuye su carga, por disminución de consumo
- la turbina cierra algunas válvulas de vapor para mantener la frecuencia entregada a la red-
- por esto, aumenta la presión  en la caldera que debe disiminuir el flujo de combustible
- en cascada, se activa la válvula de agua de la caldera y la de salida de gases de combustión hasta que la presión en el domo superior de la caldera se restablece en un valor adecuado

Todos estos controles se realizan mediante sensores y actuadores mecánicos, neumáticos y electromecánicos controlados por una computadora.

# Circutio de aire y gases de la combustión

El aire usado para la combustión se toma de la atmósfera con un ventilador de tiro forzado. Una vez que sale de la caldera, al estar caliente, se lo recircula al precalentador para recuperar algo del calor remanente.

Una vez realizada la combustión, los gases de salida son aspirados hacia una chimenea y a la atmósfera mediante un ventilador de tiro inducido.

## Centrales a carbón: Eliminación de cenizas

Los deshollinadores tienen como objetivo filtrar las cenizas antes de su salida a la atmósfera. Los hay

1. Centrífugos
2. Electrostáticos

Los centríguos emplean la rotación de los gases de salida en donde la partículas más contaminadas son dirigidas hacia las paredes y luego colectadas para su desecho.
En el caso electrostático, como las partículas contaminadas suelen tener carga negativa se las "aspira" colocando un sistema de condensador cargado y conectado a tierra.
Como el segundo es mas caro pero más eficiente (80-90%), se suelen emplear en conjunto para mejorar el rendimiento

## Ventiladores y chimeneas

Los ventiladores son de **tiro forzado** cuando envían el aire a la caldera y de **tiro inducido**  cuando lo aspiran camino a la chimenea. Éstos últimos están a efectos de no necesitar chimeneas excesivamente altas y caras para evacuar los gases a auna altura adecuada.

# Circuito de vapor

Las centrales de vapor operan bajo un ciclo rankine y su eficiencia se maximiza al hacer lo propio con el área bajo la curva del ciclo, tal como en cualquier ciclo térmico. Algunas de las acciones que llevan a esto son:

1. Reducir la presión de escape de la turbina
2. Aumentar la presión en la caldera
3. Aumentar la temperatura de sobrecalentamiento
4. Sobrecalentamiento intermedio (interesante pero sólo a gra escala)
5. Regeneración o precalentamiento con purgas (la más usada)
6. Ciclos binarios (no usados en la práctica: dos ciclos rankine uno tras otro con dos fluidos diferentes)

## Generadores de vapor (calderas)

Hay tres tipos

- Circulación natural
- Paso forzado
- Circulación forzada

![](/images/calderas.png)


### Circulación natural

Trabajan a menor presión por restricciones propias del funcionamiento (180 kg/cm^2). EL agua es llevada por bombas a la caldera que ingresa a una presión levemente superior a la de adentro (por seguridad). Es circulada hacia el domo superior y colectada hacia el inferior repitiendo el ciclo hasta que se vaporiza (al atravesar finalmente el sobrecalentador) y es usada para alimentar la turbina. A grandes presiones las burbujas de aire están muy comprimidas para que se produzca el ascenso por diferencia de densidad se requerirían calderas muy altas.

### Paso forzado

En lugar de domos hay caños que elvan el agua hasta la temperatura de vapor según el diseño, y la circulación queda a cargo de las bombas que alimentan la caldera, pudiendo diseñarse geométricamente como mejor convenga. Se usan presiones mas altas y son más económicas.
Sin embargo, ante una falla del sistema de alimentación de agua, se producen grandes daños a la instalación al fundirse los caños hervidores por falta de agua.

### Circulación forzada

Es una caldera de circulación natural a la que se le ubican bombas en el domo supperior se le adosa una bomba de circulación para compensar la falta de diferencia de densidad debida al aumento de la presión. Si bien es más caro, compensa el no tener que aumentar la altura de la caldera.

## Turbinas

El rendimiento actual de una turbina, ronda el 80%. Los alabes de una turbina pueden ser:

1. de acción
2. de reacción

Los fijos provoan un aumento de la velocidad (una disminución de presión y temperatura) mientras que los moviles le hacen perder velocidad y presión por lo que aumenta el volumen, haciendo que la sección de la turbina se vaya agrandando a medida que el vapor circula por ella.

Se escalonan varias etapas de álabes que funcionan a diferentes intervalos de presion y temperatura en donde se reinyecta vapor que se vuelve a calentar para aprovechar al máximo la energía disponible.

Las turbinas de vapor:

- son seguras, de poco mantenimiento (1 vez al año)
- son de marcha regular (es fácil acomodar la velocidad de giro)
- los servicios auxiliares usan un bajo porcentaje de la energia generada, pero aumentan su eficiencia en mayor proporción.

## Condensadores y precalentadores

Ubicados debajo de las turbinas, captan el vapor y lo condensan para reiniciar el ciclo de generación. Los hay de dos tipos

1. De mezcla
2. De superficie

### De mezcla

El vapor se pone en contacto directo con el agua de refrigeración, que transfiere calor con un 100% de eficiencia, sin embargo, el agua ahora está "contaminada" con sales y aire difcil de evacuar antes de reinyectar al ciclo nuevamente. Por esto mismo casi no se usan

### De superficie

Se usan intercambiadores de calor y el vapor condensado en agua es succionado por eyectores o bombas de vacío que lo redirigen al inicio del ciclo. El agua del circuito refrigerante no forma parte del circuito principal.

## Precalentadores de agua

Se extrae vapor en varias parte del ciclo para recalentarlo y reinyectarlo mejorando así el rendimiento del ciclo. Estas *purgas* son económicamente viables hasta 8 veces en un mismo ciclo.

Para precalentar agua si se usan condensadores de mezcla ya que ambos fluidos en contacto son de igual calidad (son agua del ciclo de vapor y ninguno contamina de más al otro).

### Desgasificador

Elimina $O_2$ y $CO_2$ del agua de alimentación mediante una combinación de métodos mecánicos y químicos reduciendo los niveles de O unas 60 veces con métodos mecánicos y hasta 300 si consideramos los químicos.

### Evaporador 

El agua del circuito puede perderse en purgas, fuga y usos auxiliares, al ingresar agua de reposición se la trata con el evaporador para quitar sales no deseadas evitando incrustaciones y daños en las cañerías de la caldera.

## Bombas de agua

### Bomba de alimentación de la caldera

Bomba que alimenta la caldera desde el desgasificador. No puede interrimpir su funcionamiento. Son de varias etapas y siempre se debe tener una auxiliar para emergencias que funciona con motor eléctrico o con vapor de la misma caldera.

### Bombas de extracción del condensador, del evaporador y de drenaje de precalentadores

La bomba de **extracción** Lleva agua del condensador (debajo de la turbina) hasta el desgasificador y trabajan a bajas presiones lo que reduce su vida útil. La de **alimentación del evaporador** llevan agua dura dentro del evaporador. Finalmente las de **drenaje de los precalentadores** toman el vapor que condensa en el intercambiador para llevarlo nuevamente al circuito principal de trabajo.

### Eyectores de vapor

Funcionan como toberas con tomas puestas a fines de generar vacíos en las etapas que se requiera una diferencia de presión que obligue o ayude al flujo en cierto sentido y lo impida en el contrario.

# Circuito de agua de refrigeración

Abierto: toma agua de un maro/rio/lago y la devuelve al mismo
Cerrado: La bomba de toma agua de la torre de enfriamiento o piletas de refrigeración y las devuelve luego atravesar el consensador (y servir de refrigeración).

## Torres de enfriamiento

Cuando el circuito de agua es cerrado se necesita refrigerar el agua de enfriamiento exponiéndola a una superficie libre o pilet de enfriamiento antes de volver a ingresarla al ciclo. Un diseño mejorado es usar una torre en donde el agua es seccionada y expuesta a un recorrido vertical en contacto con el aire que va enfriándola.

### de tiro natural

En la forma de un cilindro hiperbólico de mayor sección en la base donde se admite el aire que se acelera por efecto de la disminución de la sección hasta un punto en donde esto se revierte para evitar "salpicar" hacia afuera, ya que el agua es rociada desde la parte superior y recojida en un pozo debajo de la chimenea. Al ser de gran altura la humedad que se ve en su cima no interfiere con el ambiente.

### de tiro forzado

Se incorporan ventiladores en dos ejes en el recorrido de la torre haciendo que puedan ser muy pequeñas y más baratas, aunque incorporan material eléctrico que consume energía y debe ser mantenido (los ventiladores)

## Refrigeración por circuito cerrado

Cuando el agua es de mala calidad o no hay suficiente disponible se emplean circuitos cerrados de refrigeración con intercambiadores de calor.

## Tratamiento del agua de refrigeración

En los circuitos abiertos los tubo del condensador suelen ensuciarse debido a la presencia de bacterias y sales, para lo cual es necesario efectuar un tratamiendo de limpieza con cloro, manteniendo el ph en niveles adecuado. En los sistemas cerrados es mas común la formación de sales de calcio y magnesio por lo que se requiere un tratamiendo químico del agua antes de ingresarla al sistema.


# Circuito eléctrico

## Alternadores

De pocos polos 4 o 2, de tipo liso o cilíndrico. Trabajan a altas velocidades de rotación (1500 a 3000 rpm). Se los denomina comúnmente **turboalternadores**. La eficiencia eléctrica está cercana al 100% (98%)

### Refrigeración de turboalternadores

Para pequeñas y medianas potencias se lo logra mediante ventiladores devolviendo el aire saliente a la misma sala de máquinas si no es una muy grande, o al exterior si la envergadura lo requiere.
Para grandes potencias se usan sistemas de ventilación cerrados más eficientes y también mas costosos y seguros. Otros métodos con refrigración líquida directa interna (aceite o agua) han conseguido obtener más potencia aún a la salida


### Tensión en turbo alternadores

A mayor potencia mayor tensión, aunque para potencia no muy altas el valor de media tensión normalizado del lugar es de importancia a la hora de elegir una tensión de trabajo. A una mayor tensión hay menos pérdidas pero mayor costo en aislación.

## Transformadores

Se suelen unir a los alternadores son de gran potencia refrigerados con aceite, se ubican a la intemperie con un sistema anti-incendios. Pueden ser trifasicos o monofásicos dependiendo de la instalación.

# Consideraciones ecológicas

- Calentamiento dañino de ríos con caudal insuficiente
- Pérdida de agua por evaporación en los sistemas de enfriamiento
- Lluvia ácida si el combustible es carbón, fuel-oil, etc.
- Calentamiento global $CO_2$