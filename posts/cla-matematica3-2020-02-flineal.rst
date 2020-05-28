.. title: Función lineal (intro)
.. slug: cla-matematica3-2020-02-flineal
.. date: 2020-05-21 10:20:04 UTC-03:00
.. tags: 
.. category: matematica3
.. link: 
.. description: 
.. type: text
.. hidetitle: true
.. has_math: true
.. template: postb.tmpl

*******************
Relaciones lineales
*******************

.. admonition:: Objetivos

	- Interpretar las soluciones de una ecuación lineal gráficamente
	- Tener una noción de la relación entre varaibles
	- Conocer el concepto de variable
	- Recordar idea de perpendicularidad


En los últimos días estuvimos trabajando ecuaciones lineales.
para repasar que son podríamos decir que:

	- Aparecen números y letras
	- Las letras no están elevadas a potencias (bueno a la potencia 1 si somos rebuscados en como decirlo)
	- La cantidad de **Variables** o **incógnitas** es la cantidad de letras que hay en la expresión 

Por ejemplo esto es una ecuación lineal

.. math::
	
	3x+2y=3

Y esta otra también

.. math::
	
	\frac{2}{3}x=6

Y esta otra tambien:

.. math::

	3x+2z+y=3

Como ésta última no veremos ninguna por ahora, así que a no asustarse.


Analicemos un poco la segunda: acá la variable :math:`x` 
puede tener un sólo valor. Existe un sólo número que hace que la
igualdad se cumpla

.. math::

	\begin{aligned}
	\frac{2}{3}x&=6 \\ \cr
	\frac{2}{3} \cdot \frac{3}{2}x &=6 \cdot \frac{3}{2} \\ \cr
	x&=9\\
	\end{aligned}


La interpretación
=================

Esto nos dice entonces que para esta ecuación, sólo tenemos un posible
valor par $x$, una vez que lo encontramos, no hay mucho mas que analizar. En términos textuales, 
hemos resuelto esto:

	¿Cuál es el número que mupltiplicado por :math:`\frac{2}{3}`
	nos da $6$?


En cambio ¿que pasa con la primera ecuación? Si elijo un valor para
:math:`x`(digamos 0)  obtengo una ecuación como la primera, donde puedo despejar
$y$ y *hacer la cuenta* para obtener un valor para :math:`y`.

.. math::

	\begin{aligned}
	3\cdot 0 +2y=3 \\
	2y=3 \\
	y=\frac{3}{2}
	\end{aligned}

Esto, podríanos hacerlo para cualquier valor de :math:`x` que quisiéramos y obtendriamos
valores de :math:`y` para cada uno de ellos.

.. tip::

	Los valores de :math:`x` e :math:`y` están vinculados, si decido uno
	de ellos, el otro queda definido.


La tabla
========

Si uno hace varias veces esto de *elegir* un valor para :math:`x` y ver cuál es el
de :math:`y` que aparece (o al revés, escoge uno para $y$ para ver que $x$ nos da)
y los ubica en una tabla obtiene algo como esto:


+----+------+
| x  | y    |
+====+======+
| -3 | -6   |
+----+------+
| -2 | 4,5  |
+----+------+
| -1 | 3    |
+----+------+
| 0  | 1.5  |
+----+------+
| 1  | 0    |
+----+------+
| 2  | -1,5 |
+----+------+
| 3  | -3   |
+----+------+

.. raw:: html

	<br>

Esta tabla podría *segur por siempre*, es decir, podríamos usar cualquier número como 
valor de entrada y obtendríamos un infinitos pares asociados. Para cada $x$, hay una $y$.

	Una ecuación lineal con dos varaibles, tiene infinitas soluciones
	son todos los pares $x$ e $y$ que cumplen con la igualdad (o sea los que
	obtenemos de despejar una de las dos variables y resolver)


El gráfico
==========

Si ubicamos en un par de ejes perpendiculares (o sea, que forman **90 grados entre sí**) 
los pares de valores :math:`x` e :math:`y` obtenemos esto:

.. raw:: html

	<iframe src="https://www.desmos.com/calculator/opqgkrdzzo" width="100%" style="min-height:400px"
	style="border: 1px solid #ccc" frameborder=0></iframe>

Por convención, se usa el eje horizontal para la letra :math:`x` y el vertical para :math:`y`.
Tanto esto, cual es horizontal o cual vertical, y mismo el uso de las letras :math:`x` e
:math:`y` es absolutamente arbirtario. Podríamos decir que:

	A la comunidad matemática se le canto
	el quinto f\*\*\*o del c\*\*o usar estas
	letras y también decidió lo que le pintó
	para la ubicación de las letras en los ejes.

Esto quiere decir que, en realidad, no hay nada especial en los nombres y que 
uno podría usar cualquier letra y ubicar en el eje horizontal o vertical
la que quisiera, siempre y cuando quede debidamente explicado en el gráfico.



Resumen
=======

Juntando todo lo que acabamos de ver: 

	1. Una ecuación lineal tiene como solución infitos pares de valores
	2. Esos pares de valores, graficados, forman una línea recta





