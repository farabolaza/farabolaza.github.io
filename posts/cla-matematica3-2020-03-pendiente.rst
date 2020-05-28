.. title: La recta en forma pendiente-intersección
.. slug: cla-matematica3-2020-03-pendiente
.. date: 2020-05-28 11:35:57 UTC-03:00
.. tags: 
.. category: matematica3
.. link: 
.. description: 
.. type: text
.. hidetitle: true
.. has_math: true
.. template: postb.tmpl

*******************************
La pendiente de una línea recta
*******************************

.. admonition:: Ojbetivos de esta clase

	1. Conocer y diferenciar *Variable* y *Parámetro*
	2. Interpretar la ecuación de la recta en forma pendiente/intersección

Repaso
======

Vimos previamente que una ecuación lineal de dos variables tenía como
gráfico una línea recta, y que sus infinitos pares solución eran los que,
cuando los ubicabamos en un par de ejes coordenados (o ejes de coordenadas
o `ejes cartesianos`_ como prefieran llamarles) nos daban como dibujo una
línea recta.

.. _ejes cartesianos: https://es.wikipedia.org/wiki/Coordenadas_cartesianas 

Una ecuación podría ser ésta:

.. math::
	
	2y+1=3x

Podemos, para facilitarnos el trabajo de "armar" la tabla de valores solución
despejar una de las dos **variables** (o sea las letras $x$ e $y$ en este caso).

Voy a despejar la $y$:


.. math::
	
	\begin{aligned}
	2y+1&=3x \\
	2y&=3x-1 \\
	y&=\frac{3}{2}\cdot x -\frac{1}{2} \\
	\end{aligned}

Esto hace más facil saber "cuál es el valor de $y$ cuando hago que  $x$ sea 
cierto valor", por ejemplo, supongamos que quiero saber cuánto debe ser $y$
cuando $x$ es $0$.

.. math::
	
	\begin{aligned}
	y&=\frac{3}{2}\cdot x -\frac{1}{2} \\ \cr
	y&=\frac{3}{2}\cdot 0 -\frac{1}{2} \\ \cr
	y&= -\frac{1}{2} \\
	\end{aligned}


Por lo que el par :math:`(0,-\frac{1}{2})` es solución de la ecuación y por 
lo tanto, un punto del gráfico de nuestra recta. También lo es el punto
:math:`(1,1)`

Una recta es **algo que nunca se dobla**, y aunque esto parece una
estupidez no es así; como **nunca se dobla** todos los puntos que hacen una línea
estan todos *en fila* uno atrás de otro, **alineados**. Vean que estoy
diciendo cosas que parecen ser `redundantes`_ pero que su buena interpretación
nos lleva esto:

	Para gráficar correctamente una línea recta, sólo necesito conocer
	dos puntos que le pertenezcan

Uno marca los dos puntos (cada punto tiene un valor de $x$ y otro de $y$) 
en un par de ejes, y luego traza con regla o con imaginación, o con un software
una línea que une esos dos puntos.

	De las infinitas rectas que hay, existe **sólo una** que pasa 
	por esos dos puntos, y es la que uno acaba de dibujar


Mira ahora el gráfico 

.. raw:: html

	<iframe src="https://www.desmos.com/calculator/gdsendixrt" width="100%" style="min-height:400px"
	style="border: 1px solid #ccc" frameborder=0></iframe>


¿Tiene sentido lo que estuve diciendo hasta ahora? Tratá de imaginar otra recta, diferente
a la del gráfico y que **También pase por los dos puntos que dije más arriba**


.. _redundantes: https://www.google.com/search?sa=X&biw=1448&bih=935&sxsrf=ALeKk01nkFRbaajQWzWAwpGBjirhZSYOSQ:1590677787681&q=Diccionario&stick=H4sIAAAAAAAAAONQesSoyi3w8sc9YSmZSWtOXmMU4-LzL0jNc8lMLsnMz0ssqrRiUWJKLeZZxMoNFEsGi2XmAwCSYWV3OAAAAA&zx=1590677791312#dobs=redundante


La pendiente
============

Ahora, mirá este gráfico donde hay varias rectas:

.. raw:: html

	<iframe src="https://www.desmos.com/calculator/nbxofqsunr" width="100%" style="min-height:400px"
	style="border: 1px solid #ccc" frameborder=0></iframe>

¿Qué es lo que hace que algunas sean mas "empinadas" hacia arriba (si las miramos de izquierda 
a derecha, por ejemplo)? ¿Que hace que algunas apunten "para abajo"? ¿Por que algunas apuntan
*mas* para arriba (o abajo) que otras?

Mirá el recuadro, ¿en qué se parecen y en que se diferencian estas ecuaciones?

1. :math:`y=3x`
2. :math:`y=-x`
3. :math:`y=\frac{1}{4}x`
   
Ahora ¿en que se diferencian de esta otra?

1. :math:`y=\frac{3}{2}x+-\frac{1}{2}`

.. important::

	Las respuestas las vamos a analizar en una actividad, así que simplemente quiero
	que pienses.

Variables y parámetros
----------------------

Hasta ahora, usé la palabra **Variable** para referirme a las letras $x$ e $y$ que usamos 
en las ecuaciones. Se las llama variables, justamente porque al *Variar* sus valores
vamos construyendo el gráfico (quen o es otra cosa que un dibujo de todas las soluciones
de la ecuación). Reitero:

	El gráfico de la recta **es** un dibujo de todos los puntos solución de la
	ecuación. Gráfico, recta y soluciones **son** la misma cosa.

Se suele además ser mas específico y llamar a una *Variable dependiente* y la otra
variable *independiente* ¿por qué?, veamos esta ecuación:

.. math::
	
	y=3x +2

En esta ecuación, la $y$ aparece despejada (aislada) por lo que para 
encontrar un punto solución, podemos dar un valor a $x$ (cualquiera por supuesto)
y cuando hacemos eso, una vez que elgimos ese valor (y hacemos la cuenta), ahora, el de $y$
**depende** del valor de $x$ que hayamos elegido. Supongamos que doy a $x$ el valor $1$


.. math::
	
	y=3\cdot 1+2


.. math::
	
	y=5

Una forma de pensarlo, es que uno "mete" un valor de $x$ y a la salida obtiene un
valor de $y$, por lo que el valor de $y$ (salida) **depende** del valor de $x$ (entrada)

Esta forma de escribir las escuaciones, se suele llamar "función". No me voy a detener
en la formalidad de las funciones por ahora, pero queda claro que los valores de $y$
están en función (ya que dependen) de los valores de $x$ que uno elija poner "como entrada".

Usar $x$  o $y$ como valor de entrada o de salida, o sea, la variabla la que uno decide 
darle valores para saber cuanto vale la otra, es decisión de uno. A veces conviene
hacerlo de una forma y a veces de otra, pero si recuerdan que el gráfico de la recta
tiene que ser el mismo, porque los puntos solución son los mismos, y por lo tanto
estamos hablando de la misma línea, da igual como lo hagamos, tenemos que obtener
lo mismo como resultado.

	Los pares de puntos solucíón se pueden obtener tomando como valor 
	de entrada (variable independiente) las $x$, quedando así el valor de $y$
	como salida (variable dependiente), pero también se puede hacer al revés

Parámetros
==========

Tenemos ahora el siguiente gráfico

.. raw:: html

	<br>
	<iframe src="https://www.desmos.com/calculator/57x85okl3x" width="100%"
	style="min-height:400px" style="border: 1px solid #ccc" frameborder=0></iframe>
	<br>

Y el gráfico tiene un control que nos permite cambiar el número que multiplica 
a la $x$ desde $-10$ a $10$ ¿Qué cambia en la recta cuando damos a el parámetro
$m$ diferentes valores?

Una pregunta que te podrás estar haciendo ahora, es ¿cuál es la diferencia
entre dar valores a $x$  y obtener $y$ y lo que hacemos cuando usamos el 
control del gráfico de arriba?

Cuando lo que hacemos es encontrar los pares $(x, y)$ que satisfacen la
ecuación, o sea, que forma una recta, estamos "averiguando" de que recta
en particular se trata, digámoslo de otra manera: conocer los puntos de
la recta, nos dice *cual recta es* de todas las que existen, en cambio,
cuando cambiamos el parámetro de arriba, como verán, estamos alterando
la recta ... estamos generando una nueva recta, que tendrá por lo tanto
diferentes puntos solución, que, cuando los pongamos en un dibujo, serán
los que forman la imagen que vemos en la pantalla.

Cada vez que tocamos el parámetro $a$ del gráfico de arriba, estamos
creando una **nueva** recta que tendrá sus pares $(x,y)$, y que serán 
por lo tanto diferentes a los puntos de la anterior, porque estamos
ante una recta diferente.

.. hint::

	Usamos la palabra **variable** para las letras que representan
	a los pares de puntos que son solución de la ecuación, y que 
	graficados construyen la recta. Y usamos la palabra **parámetro**
	para aquellos elementos que nos permiten construir diferentes
	rectas.

Ecuación genérica
=================

¿Hay una forma de escribir una recta que sea a su vez "todas las rectas",
una especie de recta "genérica"?
Si, la hay, hay varias, y una es esta:

.. math::
	
	y=m\cdot x +b

¿Cómo interpreto esta cosa?

Tenemos nuestras variables, $x$ e $y$, y luego dos letras, $m$ y $b$ que son
parámetros. ¿Parámetros que hacen que cosa?

Bueno, en principio si decido dos números cualesquiera para $m$ y $b$, obtengo
una recta en particular. Por ejemplo $m=2$ y $b=4$.

.. math::
	
	y=2x+4

Así, eligiendo valores para $m$ y $b$ uno puede *generar* todas las rectas 
posibles del universo, mientras uno va pasando por todas las posibles 
combinaciones de números que se nos ocurran.


El otro parámetro
-----------------

¿Que cambia en una recta cuando cambiamos $b$?

.. raw:: html

	<br>
	<iframe src="https://www.desmos.com/calculator/rsd0319jy1" width="100%"
	style="min-height:400px" style="border: 1px solid #ccc" frameborder=0></iframe>
	<br>


Si tuvieras que decir ¿Que función cumple el parámetro $b$? ¿Cómo se 
vincula con el punto de la recta $(0,b)$?

Juntando todo
=============

Los parámetros que construyen las ecuaciones, nos permiten entender cómo
están construidas las rectas y en qué se diferencian o parecen.

En la ecuación "genérica" el parámetro $m$ se le llama **pendiente**
y al parámetro $b$ se le llama **ordenada al origen** o **intersección con el eje vertical**
o **término independiente**.

Sin importar el nombre que usemos para los parámetros, podemos sumar una
interpretación mas a todo el tema este de las ecuaciones de las rectas.

Lo relevante es entender e interpretar que rol juega cada parámetro mas allá de su
nombre, y que cambia cuando uno los modifica.

- ¿Cómo es una recta con pendiente igual a cero?
- ¿Cómo debe ser una recta para que pase por el centro de coordenadas, es decir
  el punto $(0,0)$
- ¿Cómo influye el signo de la pendiente? ¿Y su valor absoluto? (es decir si es
  muy grande o muy chico sin importar el signo)



