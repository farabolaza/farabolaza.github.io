.. title: La fase exponencial de una enfermedad
.. slug: cla-matematica5-2020-03-exponencial
.. date: 2020-03-26 22:34:22 UTC-03:00
.. tags: 
.. category: matematica5
.. link: 
.. description: 
.. type: text
.. has_math: true




***********************
Planificado la pandemia
***********************

En esta parte del trabajo vamos a intentar generar una predicción
de la fase de crecimiento exponencial del coronavrius y les voy a pedir
3 escenarios posibles para nuestro país. Para poder conseguirlo, tenemos 
que manejar ciertas herramientas.

En términos pedagógicos esto sería:

.. admonition:: objetivos
	
	- Calcular la tasa de crecimiento entre períodos para una serie de datos	-
	- Escribir diferentes escenarios de la fase exponencial de desarrollo
	- Usar la inversa (logaritmo) para averiguar *r*
	- 

Procedimiento
=============

Vamos a leer el artículo continuación del de la semana anterior `aca <https://medium.com/tomas-pueyo/coronavirus-el-martillo-y-la-danza-32abc4dd4ebb>`_
luego de eso vamos a responder la siguientes preguntas.

Preguntas
---------

Responder las siguientes preguntas:

1. ¿Qué países adoptaron medidas de mitigación y cuales de supresión?
2. ¿Cuántas `camas <https://datos.bancomundial.org/indicador/SH.MED.BEDS.ZS?view=chart>`_ por habitante tienen España, Italia, Chile, Brasil, Argentina, China y Estados Unidos?
3. ¿Cuál es la tendencia de cada país desde los 60?
4. ¿Cuánto duró el período de supresión de contacto en Wuhan?
5. Definir *R*. (Según el artículo)
6. ¿Cuál sería el proposito de una estrategia de supresión de contacto en relación a *R*?
   
Una aclaración **importante** la letra **R** que se usa en este artículo
refiere a la cantidad de contagios que **una** persona puede causar, 
mientras que usualmente el la letra $r$ se usa para medir la razón a la cual
crece una cantidad, es lo que vimos en el clase anterior: si tenemos una 
secuencia 3,9,27, la razón $r$ es 3 porque cada valor próximo se obtiene
multiplicando al anterior por 3. 

Este número es de **Vital** importancia ya que nos dice que tan rápido se
está expandiendo la enfermedad, es decir que tantos infectados tenemos
a medida que avanza el tiempo. 

Por ejemplo, una cantidad que se triplica cada "t" días, nos queda:

.. math:: 
	
	C(t)=r^t=3^t

Si pensamos en términos de días, y comparamos por ejemplo la cantidad de
infectados entre dos días sucesivos y tenemos 100,200 significa que los
infectados se duplican cada día .. por lo nuestro **modelo** sería una
exponencial de base 2. Dos multiplicado por si mismmo todas las veces que uno quiera.

.. math::
	
	I(d)=100\cdot 2^d

100 séría nuestro valor inicial, y cada día que pasa, se duplica. Un
escenario de catástrofe a todas luces. Pero no hace falta llegar a tanto,
como vimos, se llega a un escenario igual de caótico con un r bastante 
más chico.

Ahora, 

Si suponemos que los casos de duplican cada 3 días ... implica que vamos a
multiplicar por 2 nuestra cantidad cuanto el tiempo sea alguno de los 
múltiplos de 3: 3,6,9,12,etc.

¿Qué modificación tendríamos que hacer a la expresión anterior (la de $2^d$?)

Tenemos que modificar el exponente, para que sea igual a 1, si pasan 3 días,
igual a 2 si pasan 6, igual a 3 si pasan 9 e igual a 12 si pasan 4.... 
Hagamos una tabla:

.. table:: otra relación funcional
	:align: center

	+------+----+
	| dias | ex |
	+======+====+
	| 3    | 1  |
	+------+----+
	| 6    | 2  |
	+------+----+
	| 9    | 3  |
	+------+----+


En la izquierda tenemos los días y a la derecha lo que debería aparecer en
el exponente ¿que operación hay entre ambos números? ¿cuál es su relación
funcional? ... piense, vamos.

Bueno, por si no lo vieron, al número de la izquierda siempre se lo divide 
por 3, que es justamente la cantidad de días que pasan entre duplicación y
duplicación. Esto nos dice que nuestro esponente es entonces 
:math:`\frac{d}{3}`

Y nuestra función:

.. math::

	I(d)=100 \cdot 2^{\frac{d}{3}}


Ejercicios de prueba
^^^^^^^^^^^^^^^^^^^^

1. Escribir una función exponencial de valor inicial 200 y que se duplica cada 3 días
2. Escribir ua función exponencial de valor inicial 1 y que se triplica cada 2 días
3. Escribir una función exponencial de valor inicial 1 y que se duplica cada 10 días
   
.. hint:: 
	
	El tiempo en días es tu variable, valor incial refiere
	al valor de la función para el tiempo cero.



Modelame así
============

Así como recién vimos que podemos representar las situaciones de
crecimiento exponencial en base a considerar que tan rápido crece
el fenómeno que estudiamos. Usémoslo para estudiar como crecen los
casos de coronavirus en nuestro país y en otros.

Los números por estos pagos
---------------------------

.. table:: Casos de coronavirus en Argentina. 
	:align: center

	+------------+--------------+-------------+------+
	| Fecha      | Casos nuevos | Total Casos | r    |
	+============+==============+=============+======+
	| 02/03/2020 | 1            | 1           |      |
	+------------+--------------+-------------+------+
	| 03/03/2020 | 0            | 1           | 1,00 |
	+------------+--------------+-------------+------+
	| 04/03/2020 | 0            | 1           | 1,00 |
	+------------+--------------+-------------+------+
	| 05/03/2020 | 0            | 1           | 1,00 |
	+------------+--------------+-------------+------+
	| 06/03/2020 | 1            | 2           | 2,00 |
	+------------+--------------+-------------+------+
	| 07/03/2020 | 1            | 3           | 1,50 |
	+------------+--------------+-------------+------+
	| 08/03/2020 | 3            | 6           | 2,00 |
	+------------+--------------+-------------+------+
	| 09/03/2020 | 5            | 11          | 1,83 |
	+------------+--------------+-------------+------+
	| 10/03/2020 | 2            | 13          | 1,18 |
	+------------+--------------+-------------+------+
	| 11/03/2020 | 2            | 15          | 1,15 |
	+------------+--------------+-------------+------+
	| 12/03/2020 | 10           | 25          | 1,67 |
	+------------+--------------+-------------+------+
	| 13/03/2020 | 3            | 28          | 1,12 |
	+------------+--------------+-------------+------+
	| 14/03/2020 | 11           | 39          | 1,39 |
	+------------+--------------+-------------+------+
	| 15/03/2020 | 11           | 50          | 1,28 |
	+------------+--------------+-------------+------+
	| 16/03/2020 | 9            | 59          | 1,18 |
	+------------+--------------+-------------+------+
	| 17/03/2020 | 14           | 73          | 1,24 |
	+------------+--------------+-------------+------+
	| 18/03/2020 | 18           | 91          | 1,25 |
	+------------+--------------+-------------+------+
	| 19/03/2020 | 31           | 122         | 1,34 |
	+------------+--------------+-------------+------+
	| 20/03/2020 | 30           | 152         | 1,25 |
	+------------+--------------+-------------+------+
	| 21/03/2020 | 67           | 219         | 1,44 |
	+------------+--------------+-------------+------+
	| 22/03/2020 | 41           | 260         | 1,19 |
	+------------+--------------+-------------+------+
	| 23/03/2020 | 36           | 296         | 1,14 |
	+------------+--------------+-------------+------+
	| 24/03/2020 | 86           | 382         | 1,29 |
	+------------+--------------+-------------+------+
	| 25/03/2020 | 117          | 499         | 1,31 |
	+------------+--------------+-------------+------+

La última columna es la división entre los casos del día, y los del
día anterior, lo ue nos daría un "r" diferente para cada día y podríamos
a patir de esos datos proyectar hacia futuro, por ejemplo, si tomamos como
día cero el 22 de marzo la función que modelaría los próximos contagios es

.. math:: 

	C(d)=296\cdot (1,14)^d

Si en cambio tomamos el día 24 de marzo


.. math:: 

	C(d)=382\cdot (1,29)^d

También podríamos hacer un promedio de todos los valores de "r" (que nos
da 1,34) o encontrar el "r" tal que nos de que en 23 días (del 2 al 25) se
pasó de 1 caso a 499. Es decir de un valor inicial de 1 pasamos a 499 en 23
días.

.. math::

	C(d)=1\cdot r^d

	499=1\cdot r^{23}

Lo que habría que hacer, es depejar "r" y listo. Pero no nos vamos a meter
en eso todavía.

El primer caso que se considera que no vino infectado de viaje o
que se contagió de alguien que ya vino enfermo se verificó el día
`lunes 23 <https://www.infobae.com/coronavirus/2020/03/23/nueva-fase-del-coronavirus-en-argentina-que-se-espera-a-partir-del-primer-caso-de-transmision-comunitaria/>`_ 

¿Qué cosa nos dice esto respecto de nuestros valores de "r" calculados o
aproximados en los párrafos anteriores?

Simplemente que no sirven de mucho, porque todas esas personas no se contagiaron
entre sí. Por lo que si vamos a tomar un punto de inicio, debería ser a paritr
de que se detectó el primer contagiado que no tiene relación directa algún caso
importado (o de persona cercana a un caso importado).


Algo importante sobre los modelos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vamos a explicar esto en detalle luego, pero algo que todos los modelos
matemáticos, físicos, quiímicos, biológicos, económicos, etc. tienen en
común es esto: **NO SON LA REALIDAD**. Sino que a partir de sucesivas
simplificaciones y aproximaciones, los modelos **intentan** explicar y
predecir fenónemos. Un modelo puede ser válido en cierto momento y no en
otro, cuando las suposiciones que se tomaron ya no aplican, porque hay
un cambio en el contexto, o puede incluso desde un principio se sepa que
las condiciones no se cumplen para aplicar el modelo y se lo use meramente
como una aproximación cuando nose tiene uno mejor a mano.

Siempre que seamos cuidadosos, podemos usar lo que nos venga en gana, pero
siempre se debe aclarar el rango de validez de nuestras predicciones. Esto
se puede simplificar as: "va a suceder x cosa, si se cumple que a,b,c y d" siendo a,b,c,d los hechos y suposiciones que tuvimos en cuenta.

Si luego la realidad es **muy** diferente de lo que el modelo predijo, 
puede sueceder alguna de estas dos cosas: que el modelo realmente deba
ser abandonado por completo, o que debamos revisar nuestras suposiciones:
puede que no hayamos tenido en cuenta factores de importancia, o que le
hayamos dado lugar a otros factores que no influyen en nada o que lo hacen
en menor medida de lo que uno supuso. Veamos un ejemplo estúpido:

	Si me tiro de un quinto piso cantando canciones de maluma
	y llevo puesta una remera verde, seguramente moriré.

Este caso es polémico, porque en principio, suicidarse y cantar maluma
son sinónimos, pero lo es más aún porque por mas que cantemos otra cosa
o nos cambiemos la ropa, es obvio que nuestras chances de morir son las 
mismas.Acá esamos teniendo en cuenta factores que no influyen en nada
en nuestro resultado.

Veamos otro ejemplo:

	Si una persona promedio, consume mas de x cantida de azúcar
	por día, incrementa sus chances de morir prematuramente en y %

Podemos ver si esto es cierto juntando datos de gente que murió conociendo
la cantidad de azucar que consumían, y puede que encontremos que están 
ciertamente relacionados, ahora, en una muerte prematura ¿es el único 
factor que influye? ¿hay otros factores asociados que pueden "neutralizar"
el efecto de la ingesta de azucar? En todo caso podríamos pensar que
el nivel de actividad física, el resto de la alimentación, el estilo de 
vida (si se es mas o menos sedentario) también afectan. para deshacernos
de estas "dudas" deberíamos tener a mano casos de gente de diversos grupos,
pensemos sedentarios y activos, (y que tengan en común otras cosas quizás)
que consuman azucar y que no consuman azucar  y comprararlos. Si entre 
grupos "parecidos" cada vez que inlcuimos el azucar, la mortalidad 
prematura aumenta, estamos mas cerca de convencernos de que efectivamente
hay una relación entre ambos fenómenos.

Al grano señor
^^^^^^^^^^^^^^

¿Y qué tiene que ver esto con las enfermedades? Bueno es que muchos de los modelos tienen en cuenta algunas suposiciones en las cuales se basan

- Hay cierto % de gente que se inmuniza luego de enfermarse
- El mortalidad es de tanto %
- Los días que pasa una persona internada son *x* en promedio
- La cantidad de personas que un infectado puede contagiar son 2,3
- Cuanta mas gente en contacto mayor el contagio
- El período en que una persona puede contagiar es de *z* días
- El tiempo que una persona tarda en recuperarse es *w* días

Estos supuestos pueden variar: la recuperación puede ser más rápida de lo
previsto, o puede la mortalidad no ser un % fijo (pensemos que pasa si se
comienza a saturar el sitema de salud) al depender de otros factores.

Ahora vos
=========

Bueno, en base a los datos que están diposnibles en la web, en ésta misma
página (y cualquier otra que consultes) u otras fuentes, tenes que generar
tres escenarios posibles para la fase de crecimiento exponencial del virus.

Vale aclarar una vez mas, que esta fase no puede continuar por siempre aún en
el caso en que las autoridades no tomaran ninguna medida: simplemete no puede
toda la población estar enferma al mismo tiempo (o te curas o te morís).

Lo que hay que producir es lo siguiente:

- Una función que modele el crecimiento del virus en Argentina con un creicmiento diario pesimista (pero realista en relación a lo que se sabe de otros países)
- Una función que modele el crecimiento del virus en Argentina con un crecimiento diario intermedio
- Una función que modele el crecimiento del virus en Argentina con un crecimiento diario optimista

Las justificaciones de por qué consideran el escenario pesimista u optimista o 
moderado deben estar fundamentadas de alguna forma.

**por ejemplo:**

Una función que predice un escenario pesimista: 

Tomando como día inicial el día 25 de marzo, sería

.. math:: 

	I(d)=382\cdot (1,34)^d


De continuar esta tasa de contagios, para fines de abril tendríamos mas de
2 millones de infectados, que representan el 19% de la población del area 
del gran buenos aires. Si reemplazamos $d=30$, es decir 30 días a partir del
25 de marzo

.. math::

	I(30)= 382\cdot (1,34)^{30} \approx 2.484.319

Este número supera ampliamente la cantidad de camas que existen en todo el sistema 
de salud (aproximadamente 200.000), dándose solo en un día, del día 29 al 30 casi 600.000 nuevos infectados.

Mas allá de lo poco realista de este escenario (acá se debería justificar por qué)
represnta una situación de desborde, lo que implica que un "r" de 1,34 no
es sostenible para evitar el colapso del sistema sanitario.





Links que vas a necesitar
=========================

Una buena explicación sobre fenómenos exponenciales y el inicio de
la situación en nuestro país comparado con otros `acá 1 <https://elgatoylacaja.com.ar/noticias/coronavirus-exponencialidad-y-prevencion/>`_

Datos del banco mundial sobre camas por habitante `acá 2 <https://datos.bancomundial.org/indicador/SH.MED.BEDS.ZS?view=chart>`_


Artículo continuación de los de la semana pasada `acá 3 <https://medium.com/tomas-pueyo/coronavirus-el-martillo-y-la-danza-32abc4dd4ebb>`_


Datos demográficos se pueden sacar de  `acá 4 <https://es.wikipedia.org/wiki/Gran_Buenos_Aires#Aglomerado_Gran_Buenos_Aires_(AGBA)>`_ o de la página de INDEC.

Otra información que te podría ser util
=======================================

Para poder justificar los diferentes escenarios, quizás te sea bueno conocer

- Fecha del primera caso conocido
- Fecha de la primera muerte
- Porcentaje de hospitalizados / infectados
- Porcentaje de muertos / infectados
- Infectados nuevos por día desde que comenzó en nuestro país
- Mismos datos pero para otros países donde el desarrollo de la enfermedad está mas avanzado.


Te recomiendo que te hagas favoritos con los links que encuentres,
los anotes en una planilla de cálculo online, en alguna libreta, 
papel higiénico, servilleta o en un tu mano.

.. youtube:: TggNpDnW-70
	:width: 300
