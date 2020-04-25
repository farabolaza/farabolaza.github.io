Tabla en html
=============

.. raw:: html

    <table class="table table-borderless table-responsive">
    <thead>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><span class="math">\(x^2+x+2\)</span></td>
            <td><span class="math">\(ax^2+bx+c\)</span></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>texto de prueba</td>
            <td><span class="math">\(y=a\cdot \alpha + \beta\)</span></td>
            <td>
            <button class="btn btn-success" data-toggle="collapse" data-target="#demo">Solución</button>
            <div id="demo" class="collapse">
            Lorem ipsum dolor text....
            </div>
    </div>
            </td>
            <td></td>
        </tr>
        <tr>
            <td><span class="math">\(c^2=a^2+b^2\)</span></td>
            <td><span class="math">\(z^3=x^3+y^3\)</span></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
    </table>

.. tip:: que cosa se te ocurre para 
    que puedas resolver esto

.. raw:: html

    <button class="btn btn-success" data-toggle="collapse" data-target="#demo">Solución</button>

    <div id="demo" class="collapse">
    la concha de tu madre allboys....
    </div>

como quedara?

.. raw:: html

    <iframe scrolling="no" title="Mover los parámetros y ver que pasa" src="https://www.geogebra.org/material/iframe/id/antzepsr/width/700/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/true/ld/false/sdz/true/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>

Ejercicios o examenes desde Latex
=================================


La idea sería poder convertir los exámenes y ejercitaciones escritas en Latex usando pandoc a html, para luego incluir
el archivo o parte del código, más un link de descarga, y de esta forma reutilizar el trabajo hecho en latex cuyyo destino es 
el de ser impreso.

+----------------+---------------------+
| :math:`x^2+1`  | :math:`2x\cdot y^3` |
+================+=====================+
| :math:`y=3x+2` | :math:`z_0=x_a+y_b` |
+----------------+---------------------+

.. raw:: html

    <table class="table table-borderless table-responsive">
    <table style="width:49%;">
    <colgroup>
    <col style="width: 21%" />
    <col style="width: 27%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><span class="math inline">\(x^2+1\)</span></th>
    <th><span class="math inline">\(2x\cdot y^3\)</span></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><span class="math inline">\(y=3x+2\)</span></td>
    <td><span class="math inline">\(z_0=x_a+y_b\)</span></td>
    </tr>
    </tbody>
    </table>

Empezando desde una lista
=========================

Encontrar los ceros

1. :math:`2x+1=y`


.. raw:: html

    <button class="btn btn-success" data-toggle="collapse" data-target="#demo1">Solución</button>

    <div id="demo1" class="collapse">
    la concha de tu madre allboys....
    </div>

2. :math:`y=2x`


.. raw:: html

    <button class="btn btn-success" data-toggle="collapse" data-target="#demo2">Solución</button>

    <div id="demo2" class="collapse">
    la concha de tu madre allboys....
    </div>

3. :math:`y=\frac{2}{3}x+5`


.. raw:: html

    <button class="btn btn-success" data-toggle="collapse" data-target="#demo3">Solución</button>

    <div id="demo3" class="collapse">
    la concha de tu madre allboys....
    </div>

4. :math:`2x+1=0`

.. raw:: html

    <button class="btn btn-success" data-toggle="collapse" data-target="#demo4">Solución</button>

    <div id="demo4" class="collapse">
    lcdtmab....
    </div>


Tabla en csv
============

.. csv-table:: Planificación anual 2020
    :file: files/planificaciones/plan-matematica5-2020.csv
    :header-rows: 1
    :class: longtable
    :widths: 5 5 7 15 20 20 10 10 


nav tabs para las planificaciones
=================================


.. raw:: html

    <br />
    <ul class="nav nav-tabs" id="tab1" role="tablist"> 
      <li class="nav-item">
        <a class="nav-link active" id="fc-tab" data-toggle="tab" data-target="#funciones_contenidos" role="tab" >Contenidos</a>
      </li>
      
      <li class="nav-item">
        <a class="nav-link" id="fo-tab" data-toggle="tab" data-target="#funciones_ojbetivos" role="tab" >Objetivos</a>
      </li>
      
      <li class="nav-item">
        <a class="nav-link" id="actvidades-tab" data-toggle="tab" data-target="#funciones_actividades" role="tab">Actividades</a>
      </li>
      
      <li class="nav-item">
        <a  class="nav-link" id="fh-tab" data-toggle="tab" data-target="#funciones_horas" role="tab">Horas</a>
      </li>
    </ul>
    <div class="tab-content">
      <div class="tab-pane fade in active" id="funciones_contenidos" role="tabpanel">
      Contenidos del eje funciones</div>
      <div class="tab-pane fade" id="funciones_ojbetivos" role="tabpanel">
      Objetivos del eje funciones</div>
      <div class="tab-pane fade" id="funciones_actividades" role="tabpanel">
      Actividades del eje funciones</div>
      <div class="tab-pane fade" id="funciones_horas" role="tabpanel">
      Horas del eje funciones</div>
    </div>

    <br />

y la la la

Iframe de desmos
================


.. raw:: html

    <iframe src="https://www.desmos.com/calculator/atmghogvho?embed" width="500px" height="500px" style="border: 1px solid #ccc" frameborder=0></iframe>

fin

