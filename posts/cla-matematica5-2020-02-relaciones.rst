.. title: Coronavirus y matemáticas
.. slug: cla-matematica5-2020-02-relaciones
.. date: 2020-03-18 09:42:53 UTC-03:00
.. tags: 
.. category: matematica5
.. link: 
.. description: 
.. type: text
.. has_math: true

.. admonition:: Objetivos

	- Comprender el concepto de relación funcional.
	- Escribir relaciones funcionales sencillas.
	- Reconocer en un set de datos la relación funcional que mejor 	se le ajusta,
	- Usar la función exponencial para modelar la expansión del 	coronavirus y analizar las posibles políticas publicas a adoptar.

.. contents:: En esta clase

Relaciones funcionales
======================

No, no me estoy refiriendo a pegar un buen compañero/a de truco o a
una familia en donde no hay heridos de gravedad luego de una discusión sino
a como dos (o más) grupos de datos, pueden estar relacionados entre si.

Volvamos a la primaria (no en sentido literal, los niños son muy ruidosos)
por un momento y analicemos los datos de esta tablita

.. table:: una relación
	:align: center

	+--------+-------+
	| Dato 1 | Dato2 |
	+========+=======+
	| 1      | 3     |
	+--------+-------+
	| 2      | 6     |
	+--------+-------+
	| 3      | 9     |
	+--------+-------+
	| 4      | 12    |
	+--------+-------+

.. raw:: html

	<br />
	
¿Qúe relación hay entre el *dato 1* y el *dato 2* ... musiquita de pensar 
de programa de entretenimiento de fondo ....

.. math::
	
	\text{Dato 2} = (\text{Dato 1})\cdot 3

Es decir, estamos multiplicando por 3 al *dato 1* para obtener el *dato 2*.
Hasta acá todo muy bonito. Ahora voy a apretar un poco el acelerador.

La vida humana y los procesos que generamos; relaciones interpersonales,
desastres ecológicos, patrones de sueño, de consumo, cantidad de pases a
los defensores centrales en un partido, y todo lo que se nos ocurra, 
crean una infinidad de datos, que, si los clasificamos y ordenamos de 
forma adecuada nos permiten entender lo que hacemos, lo que hicimos y lo
que va a pasar si seguimos haciendo lo mismo.

También la naturaleza y todos sus procesos biológicos, físicos y químicos
pueden ser leídos (y entendidos) si se los mira con atención, se generan 
los datos adecuados y se identifican los vínculos precisos que los
enlazan. Poder mirar con atención como algo funciona nos da la llave para
copiar, armar, romper, reproducir o detener lo que sea que nos interese.

Relaciones funcionales for dummies
==================================

Hasta ahora, en su proceso de escolarización deberían estar familiarizados
con varias relaciones funcionales, presentadas en forma abstracta
bajo el nombre de "funciones" y con una definición de este tipo:

	
	Una función es una relación entre dos conjuntos tal que
	a cdada elemento del conjunto de salida o dominio le corresponde
	uno y sólo uno de conjunto de llegada o imagen

.. image:: /images/wtf.jpg

Lo que esta definición dice es que si uno conoce el valor de entrada, y
sabe lo que la función hace (en el ejemplo anterior era multiplica por 3),
entonces deberá necesariamente saber cual es el valor de salida. Si a la
entrada tengo un 1 y se que debo multiplicar por 3, es obvio que la salida
es 3.

Una aclaración es que en la realidad, cualquier proceso puede ser pensado
en la dirección que uno quiera: la relación entre suicidios y dias lluviosos,
o la relación entre días lluviosos y suicidios. Lo que uno toma como entrada y
como salida depende de lo que se quiera estudiar y cómo. En nuestra vida es 
importante muchas veces establecer causas y consecuencias además de relaciones.

Por ejemplo, podemos relacionar *crisis económicas* y *cantidad de divorcios*. 
Todos vamos a estar de acuerdo en que es posible que exista una relación, pero
a la hora de analizar causas y consecuencias, es más fácil aceptar que las crisis
causan mas divorcios, y no que los divorcios causan crisis económicas. Aunque claro,
deberíamos profundizar para poder estar seguros.

Tipos de relaciones
-------------------

Vamos a resumir los tipos de relaciones funcionales que conocemos:


Proporcionalidad directa
^^^^^^^^^^^^^^^^^^^^^^^^

Dos cantidades o series de datos están relacionadas en proporcionalidad directa
de forma que si una aumenta la otra también, y si una disminuye la otra también lo
hace y lo hacen a un *ritmo* constante, siempre igual. 

	Si una pizza vale \$ 50. ¿Cuanto vale comprar N pizzas?

Esta relación nos lleva a una forma **lineal** donde el precio varía siempre
lo mismo en función de cuantas pizzas compremos

.. math::
	
	P(N)=250\cdot N

Puede que tengamos ademas un *valor inicial*

	La entrada al cine cuesta \$100 y el paquete de pochoclos \\\$150
	¿Cuánto gasta una persona en una salida en función de la cantidad
	de paquetes de pochoclos que se come?


.. math::
	
	S(P)=100+150\cdot P

Por supuesto que podríamos tener también una cantidad variable de personas
y esto nos llevaría a una función lineal de **más** de una variable. En el
caso del cine, tendríamos

.. math::
	
	S(P,N)=100\cdot N + 150\cdot P

Donde contamos por separado la cantidad de personas *N* que van y la de
pochoclos *P* que se comen.

Por una cuestión de simpleza, en la secundaria no se ven relaciones de mas de una
variable, aunque ciertamente considero que sería posible hacerlo, además permitiría
ver gráficos en 3D, imposibles de dibujar a mano salvo que seas un genio, hecho que
incentivaría a los establecimientos educativos a tener más dispositivos tecnológicos.

**Resumen**: Las relaciones de proporcionalidad directa, nos dan funciones lineales.

Otras proporcionalidades
^^^^^^^^^^^^^^^^^^^^^^^^

La relación podría no ser lineal, y cuando digo lineal es que la variable, en los
casos anteriores, la cantidad de personas o de pochoclos o de pizzas no esta elevada
a ninguna potencia (bueno, 1 es una potencia).

El gran Galileo Galilei, además de cargarse al bueno de Aristóteles al que todo el 
mundo le creía por una extraña mezcla de adoración y pereza intelectual, demostró
que cuando un objeto se deja caer en el planeta tierra, la distancia que recorre
es proporcional al cuadrado del tiempo que le lleva recorrerlo. Si algo se cae,
cuanto mas tiempo está en el aire es obvio que recorre mas distancia, pero en este
caso la relación ya no es lineal sino que es cuadrática.

.. math::
	
	d \propto t^2

El símbolo que está en donde uno esperaría el igual es "proporcional" lo que nos
dice es que hay una relación de cuadrado, pero para llegar a escribir la igualdad
deberíamos saber además una constante (un número) que es característico del problema.

En el caso de las cosas que caen, la constante es la aceleración de la gravedad, y en
la tierra vale aproximadamente :math:`9,8 \: \frac{m}{s^2}` entonces nos queda

.. math::
 	
 	d=9,8\cdot t^2

Por si este ejemplo te perdió un poco, vamos a uno mas geométrico: el volumen de un
objeto sin importar la forma que tenga, es proporcional al cubo de su dimensión
lineal ¿ah? y si ... si uno tiene un segmento .. volverlo 3d nos genera un cubo, y
el volumen del cubo es :math:`v=l^3`. Pero si la forma lineal no es un segmento,
podría ser cualquier otra, y el objeto a generar la forma mas loca que se nos ocurra
la proporcionalidad de "lineal al cubo" se cumple porque uno esta creando a partir
de una dimensión, un objeto en 3, lo que naturalmente implica un cubo.

.. math::
	
	V \propto L^3

Para cualquier cosa.

Entonces, ¿cual sería la proporcionalidad entre un segmento y su área? ... y si. Una
relación de cuadrado. 

*Resumen*: Además de la proporcionalidad directa lineal, tenemos situaciones
para de proporcionalidad parar otras potencias, incluso las potencias fraccionarias.

Proporcionalidad inversa
^^^^^^^^^^^^^^^^^^^^^^^^

Si hay dos cantidades que están relacionadas de manera que si una aumenta la otra
debe disminuir, estamos en un caso de proporcionalidad inversa. Esto puede también
expresarse como que el producto de ambas cantidades es constante.

Estas relaciones aparecen cuando justamente, tenemos algo que no puede cambiar,
que es constante y debe ser distribuido de alguna manera: por ejemplo, si tengo
una cierta cantidad de comida o dinero entre personas, si hay mas personas, a
cada una le toca menos, y si hay menos, cada una recibe más, pero la cantidad a
repartir es fija. Supongamos que tenemos que distribuir recursos bancarios y
tenemos $:math:`100 \cdot 10^6` y vamos a dar créditos todos del mismo monto: el
monto de cada uno multiplicado por la cantidad, deberá ser el total,

.. math::
	
	C\cdot M = 100 \cdot 10^6

Donde podemos despejar si nos interesa alguna de las dos cantidades, y nos queda

.. math::
	
	C= \frac{100 \cdot 10^6}{M}

Crecimiento exponencial
^^^^^^^^^^^^^^^^^^^^^^^

Y ahora si llegamos a la relación que nos va a ocupar el resto del tiempo. Lo más
probable es que ante la pandemia de coronavirus que nos afecta, cuyo desarrollo es
en parte exponencial, estemos compensando en medios y lenguaje común la cantidad
de veces que alguien dijo de forma completamente incorrecta que algo "creció
exponencialmente" (cuando no) como sinónimo de "se fue a la m..". Las enfermedades
SI que se expanden en forma exponencial y veremos por qué.

El año pasado seguramente habrán visto las progresiones geométricas y aritméticas.
Si no lo hicieron o no lo recuerdan no importa. Es fácil.

En una progresión aritmética (una progresión es una serie de números que sigue
algún patrón) al término siguiente se lo obtiene al sumar una cantidad fija
al anterior, por ejemplo la secuencia 1,3,5,7 resulta de sumar 2 al anterior.

En una progresión geométrica en vez de sumar, multiplicamos por un mismo valor.
Así la serie 1,3,9,27 resulta de multiplicar por 3 al número anterior. Si uno
sabe el primer valor,  y le piden que de el resultado del paso N tiene que 
multiplicar al primer valor N veces por 3. Multiplicar N veces por un mismo 
número, implica que estamos usando la operación de potencia.
:math:`3\cdot 3 \cdot 3 \cdot 3=3^4`. En tal caso, podemos escribir

.. math::
	
	P_n=3^n

Este tipo de relaciones aparece siempre que una cantidad depende de esa misma
cantidad pero en un instante o paso anterior. Voy a detenerme acá. Vean este 
video.

.. youtube:: Kas0tIxDvrg
	:align: center
	:width: 400

Las matemáticas detrás de una pandemia
======================================

Como se habrán dado cuenta, la forma en que una enfermedad contagiosa
se esparce es en principio exponencial. Pero esto no puede suceder por
siempre, es decir, las personas se curan (y se inmunizan en cierta forma), se
mueren, y la enfermedad se va quedando sin personas a las que contagiar, con
un máximo de *toda la población enferma* que luego comienza a descender.

¿Como sería un gráfico de enfermos en función del tiempo? ¿Que forma tendría?

El riesgo fundamental en este tipo de enfermedades cuya tasa de mortalidad no
es muy alta, es que tengamos picos de una enorme cantidad de gente enferma  al
mismo tiempo. Esto es un problema por varios motivos:

- satura el sistema de salud
- un sistema de salud saturado provoca mas muertes (personas que no deberían morir lo hacen, ya que le sistema colapsado elige entre pacientes)
- el colapso del sistema de salud provoca grandes perjuicios económicos
- los mismos trabajadores del sistema de salud se enferman mas, saturándolo más aún.

El objetivo de las políticas públicas deben ser la de mitigar la velocidad de 
contagio, para evitar que existan en un momento dado, mas personas enfermas de las
que el sistema de salud puede atender de forma correcta.

Esto depende muchísimos factores. Pero para tener una idea precisa, vamos a leer
estos dos artículos.

`Coronavirus Por qué debemos actuar ahora`_ 

.. _Coronavirus Por qué debemos actuar ahora: https://medium.com/@tomaspueyo/coronavirus-act-today-or-people-will-die-f4d3d9cd99ca



`Versión en castellano`_ 

.. _Versión en castellano: https://medium.com/tomas-pueyo/coronavirus-por-qu%C3%A9-debemos-actuar-ya-93079c61e200

`Coronavirus en Argentina`_ 

.. _Coronavirus en Argentina: https://medium.com/@titohubert/coronavirus-en-argentina-porque-es-clave-actuar-ya-y-no-ma%C3%B1ana-b928e7736d82

