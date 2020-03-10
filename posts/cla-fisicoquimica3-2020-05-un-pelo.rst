.. title: ¿Cuanto mide un pelo?
.. slug: cla-fisicoquimica3-2020-05-un-pelo
.. date: 2020-03-08 23:33:12 UTC-03:00
.. tags: 
.. category: fisicoquimica3
.. link: 
.. description: 
.. type: text
.. hidetitle: true
.. has_math: true

********************
Cuanto Mide un pelo?
********************

De la clase anterior quedaron dando vueltas muchas cosas que
no vamos a terminar de comprender a la perfeccción por el momento, 
pero las podemos resumir así

- la luz tiene un tamaño
- ese tamaño esta asociado a su color
- cada *color* tiene un tamaño diferente
- Este tamaño se llama *longitud de onda*
- La longitud de onda :math:`\lambda` está relacionada con la frecuenca de la oscilación de la luz
- A mayor frecuencia, menor longitud de onda

Un video que resume estas ideas

.. youtube:: nwlhAXkzjj0
	:align: center
	:width: 400

Usando esta idea de que la luz tiene un tamaño, observamos que

- Si la luz se topa con un objeto que es mucho mas grande que ella se comporta como si fuera un corpúsculo, una bolita.
- Si por el contrario el tamaño del obstáculo es "similar" (mas adelante veremos con que precisión se puede considerar algo similar o no) la luz se porta como una "onda" y provoca fenómenos extraños como interferirse a si misma, poder "bordear" un objeto (como el agua a un bote)

.. admonition:: Objetivos

	- Usar el concepto de *longitud de onda*
	- Realizar una medición
	- Estimar el ancho de un pelo
	- Usar correctamente las unidades de longitud
	- Calcular el promedio de varias mediciones
	- Entender la idea de *incerteza* de una medición
	- Uso de la calculadora en notación científica
	- Angulos en radianes

Laseres a la obra
=================

Cuando una "porción" de luz (mejor sería una porcíón de muzarella) parte
del extremo izquierdo del pelo, y otra parte del extremo derecho, como
estamos en la situación en que la luz se comporta como una onda vimos que
al llegar a la parded o pantalla, en algunos lugares se "suman" y se ve
brillante y en otros "se anulan" y hay oscuridad.

Podemos ver un esquema de esto así

.. figure:: /images/superposicion.png
	:align: center

	Esquema de superposición de ondas

Esto es una buena forma de demostrar que la luz se porta como onda y no
como una bolita ¿Podrías explicar por que?

Mirá con atención los triangulos que aparecen en la imagen. ¿Hay alguno que
sea semejante a otro?

.. figure:: /images/interferencia2.png
	:align: center
	:scale: 50 %

	Triangulos  semejantes

Volvamos, la idea **importante** es que la luz se va sumar y vamos a tener un
espacio brillante siempre que la diferencia en la distancia recorrida entre
la parte "izquierda" y "derecha" sea de 1 longitud de onda, 2 longitudes de onda
y así sucesivamente.

En matemática esto se ecribe así

.. math::
	:label: eq:interferencia
	
	a\sin\theta=n\lambda

Algo que seguramente te suena a chino, pero que vamos a explicar mejor en el
pizarrón.

Ahora, lo del :math:`\sin \theta` podemos reemplazrlo tanto por el ángulo como por 
la tangente (que es la rlación entre el cateto vertical y el horizontal).

Para una explicación sobre qué es la tangente y que es el seno, `acá <https://es.wikipedia.org/wiki/Funci%C3%B3n_trigonom%C3%A9trica#Definiciones_respecto_de_un_tri%C3%A1ngulo_rect%C3%A1ngulo>`_ 

Probá con la calculadora (tiene que estar en modo RAD) hacer

- $\sin(0,01)$
- $\tan(0.01)$

La letra $a$ de la ecuación de arriba es el ancho de nuestro pelo, lo que nos interesa.
¿Como quedaría la expresión de arriba si despejamos $a$?

.. math::
	
	a=\frac{n\lambda D}{y_n}

Procedimiento para medir
========================

La distancia al pizarron
------------------------

Medimos desde el láser al pizarrón.

Este dato es $D$

La longitud de onda del laser
-----------------------------

Ese dato esta en el laser mismo, es :math:`650\cdot 10^-9\: m`

Este dato es $\lambda$

Las distancias en el pizarrón
-----------------------------

Vamos a medir desde el centro del punto brillante hasta que empieza
la primera franja de luz.

Luego vamos a medir desde el centro hasta que termina esa misma franja.

Finalmente hacemos el promedio de ambas distancias.

Este dato es $y_n$ en nuestro caso como es la primera $y_1$

Repitiendo para otros n
-----------------------

¿Y que es la n? bueno, si medimos hasta la "2º" franja igual que en la 
anterior, donde dice "n" ponemos 2 y medimos $y_2$

Esto lo hacemos para todas las franjas visibles.

Volcando los datos
==================

Volcamos todos los datos en una tabla. ¿Te animás a diseñar como sería
esa tabla?

Haciendo cuentas
================

Finalmente, hacemos las cuentas para todos los valores, y luego, calculamos
el promedio.

¿Cuanto dio? Buscá en internet cuanto es aproximadamente el ancoh de un pelo
de una persona.

¿Que tanto le erramos?
----------------------

Una forma de saber que tan preciso es nuestro experimento es 
compararlo con el valor conocido, etablecer una relación.

Para hacer esto podemos simplemente dividir el valor que nos dió
por el valor real, ¿que estaríamos comparando en este caso?

Para saber que tanto nos alejamos del valor "aceptado" podemos 
hacer otra cuenta

.. math::
	
	\frac{\text{valor medido}-\text{valor aceptado}}{\text{valor aceptado}}

¿Que pensas que acabamos de calcular con esta cuenta de acá arriba?
