.. title: cheatsheet
.. slug: cheatsheet
.. date: 2020-01-12
.. tags: nikola, cheatsheet
.. category: 
.. link: 
.. description: 
.. type: text
.. hidetitle: true
.. template: storyb.tmpl

.. contents:: Contenido

Cómo hice esta página
---------------------

Este apartado recolecta todo lo que hice para poder armar este sitio con Nikola,
y detalla las configuraciones que tuve que hacer. El objetivo es que no me olvide de lo que hice,
como suele suceder con todo lo que no ejercito seguido. El alemán me persigue. Uh, uh, los alemanes!

Instalación
^^^^^^^^^^^

Para instalar Nikola primero que hay que tener instalado *virtualenv* en anaconda, para poder instalar los paquetes necesarios sin cagar la instalación principal de python. En `este sitio <https://randlow.github.io/posts/python/create-nikola-coding-blog/>`_ está casi todo, pero lo voy a ir traduciendo y agregando a este apartado.

Modificando conf.py
+++++++++++++++++++

Algo que Nikola te deja hacer, y es muy bueno si sos un amateur completo del diseño web, es configurar el esqueleto
de todo el sitio modificando solo algunas cosas del del archivo *conf.py*

Templates Customizados
++++++++++++++++++++++

Tanto la homepage como otras páginas se procesan usando templates modificados a los que Nikola provee. Para que una página o post
usen un template en particuar hay que modificar en el archivo '.rst' los metadatos para incluirlo, por ejemplo;

Si quiero que una página use el template 'storyb', los metadatos deben quedar asi:

.. code:: rest

	..title: titulo
	..slug: nombre que se muestra en la barra de direcciones
	..date: fecha 
	..tags: separadas por coma, una, otra
	..template: storyb.tmpl


+-----------+------------------------------------------------------------------------------------------------------------------------+
| templates | descripción                                                                                                            |
+===========+========================================================================================================================+
| hpage     | se usa en la home, 3sm izquierda y 9sm derecha, el ontenido que hay en la parte d e3sm esta hardcodeado en el template |
+-----------+------------------------------------------------------------------------------------------------------------------------+
| storyb    | genera una *page* con una barra lateral sticky que usa la tabla de contenidos del documento                            |
+-----------+------------------------------------------------------------------------------------------------------------------------+
| postb     | genera un *post* con una barra lateral sticky que usa la tabla de contenidos del documento                             |
+-----------+------------------------------------------------------------------------------------------------------------------------+

|

La estructura del sitio
^^^^^^^^^^^^^^^^^^^^^^^

Como Nikola sólo permite una categoría por POST, dejando el lugar más flexible para las TAGS, decidí que sólo las Materias sean
categorías. Cada menú de la barra de navegación, cuyo detalle se puede ver en `Modificando conf.py`_ representa un apartado que está orientado a diferentes usos. Los TAGS se usan para otras secciones que no sean específicamente material de clase de cada materia. 

La barra de navegación
++++++++++++++++++++++

El primer bloque o sección del menú contiene las **Clases** (es decir los contenidos que se dieron o darán en determinada asignatura)
y cada elemento lleva al INDEX de esa **categoría**.

- CATEGORY 1 = matematica3
- CATEGORY 2 = matematica5
- CATEGORY 3 = fisicoquimica3
- CATEGORY 4 = fisicacontempo1

El segundo bloque, **Bibliografía** está apuntando a una *tag* específica creada para la bibliografía de cada materia

- TAG 1 = bib-matematica5
- TAG 2 = bib-matematica3
- TAG 3 = bib-fisicoquimica3

El tercer bloque, **Planificaciones** hace lo propio pero con las planificaciones docentes de cada año. La estructura de nombre
para cada categoría sería:

- TAG A = plan-matematica3
- TAG B = plan-matematica5

Cada bloque subsiguiente del menú de la *navbar* utiliza la misma estructura de TAGS generadas manualmente a partir
de las categorías. Esta estructura se puede replicar todo lo necesario. Si uno quiere tener una vista "Argegada" de 
todos los posts de cierto tipo, esta bueno usar una TAG que lo haga. Por ejemplo, una TAG "planififaciones" debería
agregarse ademas de plan-matematica3 para poder visualizarlas todas juntas en el INDEX que Nikola genera automáticamente.

*pages* y *posts*
+++++++++++++++++

Como Nikola aplica toda su escturucta de BLOG para generar las páginas INDEX  de cada categoría (y de cada TAG), el año de validez 
para cada planificación, bibliografía, etc. queda determinado por la inClusión de ese dato tanto en la fecha de la publicación 
del POST como en su título, descripción, etc.

Para evitar la indexación de planificaciones, bibliografías y otros documentos junto a las clases de cada materia, los posts que no sean
estrictamente material  de aula no llevarán categoría. Solamente se llenarán los tags.

Como regla básica:

- Los POSTS es todo lo que quiero que se indexe
- Los POSTS sin categoría, es todo lo que NO es una clase
- Las PAGES son paginas que no quiero que se indexen, como esta misma.

Nombre de los archivos
**********************

La estructura de los nombres para los posts, es

::

	tipo-materia-año-numero-titulo
	plan-matematica3-2020
	cla-matematica3-2020-01-diagnostico

Links de interes
^^^^^^^^^^^^^^^^

En los siguientes links hay información interesante que voy a ir agregando.

- Plugin para sublimetext que hace mas facil trabajar con restructuerdtext `acá <https://packagecontrol.io/packages/Restructured%20Text%20%28RST%29%20Snippets#headers>`_
- `Buena guía de atajos para rest <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#inserting-code-and-literal-blocks>`_
- `una página <https://jiaweizhuang.github.io/blog/nikola-guide/>`_ con un tutorial básico sobre Nikola y links a otros tutoriales.

El flujo de trabajo
^^^^^^^^^^^^^^^^^^^

Êl contenido online se tipea en ``restructuredtext``  usando ``sublime-text`` o ``visual sutdio code``
(editor que aún no consigo hacer funcionar del toodo bien con ``restructuredtext``luego, usando ``pandoc``
se convierten  a latex para generar una versión imprimible de cada clase.
Este flujo aún está en proceso.

Los exámenes
^^^^^^^^^^^^

Los examenes se hacen en ``latex`` aprovechando la clase *exam*, para tener mas detalles de esto, va
a ser mejor tener una entrada de blog específica.

Github_deploy
-------------

En conf.py si estamos usando un repositorio de usuario, "usuario.github.io"
la rama de deploy es la master.

Si estamos usando otro repositorio la rama es "gh-pages". No olvidar darle "nikola build" luego de estos cambios.

Para que la página pueda ser publicada debemos hacer, desde el terminal y en la carpeta donde
esta nuestra página

.. code:: 

	git init .
	
	remote add origin https://github.com/usuario/repositorio.git



