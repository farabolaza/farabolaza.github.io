---
title: 01 Aprovechamiento de la energía
slug: cla-energo-2022-01-energia
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

Aprovechamiento de la energía
=============================

## Disponibilidad y necesidades energéticas

### Fuentes de energía

1. Flujo solar (**renovable**)
    1. Viento: Energía eólica
    2. Energía solar térmica
    3. Energía solar fotovoltaica
    4. Energía hidráulica
    5. Energía mareomotriz
2. Combustibles fósiles (solar acumulada **no renovable**)
    1. Petróleo
    2. Carbón
3. Biomasa (solar acumulada **renovable**)
    1. Leña
4. Geotérmica
5. Nuclear
    1. Fisión
    2. Fusión


### Consumo enrgético
1. Ser humano (metabolismo basal)
2. Ser humano (industrial)
3. Ser humano (tecnológio)


### Formas de la energía
1. Cinética
2. Potencila
3. Térmica
4. Química
5. Electromagnética
6. Lumínica
7. Eléctrica
8. Inherente a la masa ($E=mc^2$)


### Transporte y almacenamiento
Las más fáciles de transportar son los cumbustibles fósiles y el uranio

### Energía primaria
Aquellas al as que no se les modifica su naturaleza (petróleo -es discutible-). Un motor primario es uno que utiliza una energía primaria: centrales térmicas (diesel) o a gas (turbina de vapor)

### Utilidad de la energia (clasificación)

Energía útil es aquella que ocupa el último lugar antes de ser entregada al ambiente como energía térmica de baja temperatura no reutilizable.

1. Energía térmica a 20 C: calefacción
2. Energía térmica a 50 C: agua uso doméstico
3. Energía térmica a 100 C: procesos industriales
4. Energía térmica entre 100 C y 1000 C: +generación de energía
5. Energía térmica a más de 1000 C: +generación de energía
6. Energía mecánica
7. Energía lumínica

## Variación de la demanda de energía

### Potencia de cresta

Completar

## Vectores de energía
Se llama vector de energía la forma en la cual la energía es transferida de un lugar a otro. Si el vector está compuesto por materia, es posible almacenarlo. Se pueden clasificar en sólidos, líquidos, gaseosos, eléctricos, mecánicos, neumáticos, hidráulicos, elásticos, etc. Si bien la energía se puede transferir mediante radiación (tal es como nos llega del sol) no es útil en los términos de esta clasifiación puesto que para los fines prácticos humanos no se transporta energía en forma de radiación: las telecomunicaciones tienen como objeto la transferencia de información y no de energía, y por lo tanto, aunque sean radiación no se las consideran en este apartado. A la energía radiante capturada se la debe almacenar en algún otro vector para su transferencia.

## Sistema eléctrico
La energía eléctrica es otro vector de energía. El sistema está compuesto por

1. Producción
2. Transmisión, reparto y distribución
3. Consumo


## Capacidad de transmisión por vector de energía

- Un ferrocarril puede transportar carbón o combustible a un ritmo determinado por su capacida de carga y su velocidad
- Un oleoducto puede transportar petroleo a un ritmo que depende de su presión, envergadura, etc.
- Un gasoducto puede transportar gas a un ritmo que depende de su presión, envergadura, etc.
- Una línea eléctrica puede transportar energía/tiempo a un ritmo que depende de la sección de sus instalaciones, capacidad de carga, etc.


## Capacidad de almacenamiento por vector de energía

- El carbón se puede almacenar al aire libre
- Los derivados del petróleo necesitan ser guardados en recipientes espeiales
- El gas se debe depositar en recipientes específicos más caros que los anteriores (debido a que deben resistir grandes presiones y esfuerzos mecánicos) y comprimido, lo que hace esta opción mucho más cara que los anteriores ejemplos. Uso en cresta de gasómetros
- La energía eléctrica se puede almacenar sólo como continua en baterias, aunque es un método costoso y poco eficiente para escalarlo aún con los avances tecnológicos recientes.

![](/images/vectores.png)

## Potencia eléctrica y suministro eléctrico

- Tension continua
- Tensión sinusoidal
- Energía activa: la que se usa efectivamente
- Energía recativa: la que se usa para generar campos magnéticos y eléctricos en bobinas y capacitores pero que no es usada para generar un trabajo útil. Sobrecarga los sistemas y no es detectada por el medidor de consumo. Se la suele penalizar.
- Obligación de tensión constante y corriente constante
- Garantía de potencia
- Obligación de potencia activa y reactiva necesaria (para no hacer bajar la tensión)
- Factor de simultaneidad $$\frac{P_\text{max teorica}}{P_\text{max real}}$$
- Agrupando a usuarios diversos en una misma red se puede reducir el factor de simultaneidad.

### Ventajas de la CC

- Un conductor para señal y no para retorno (tierra)
- Flexbilidad de los motores de CC para regular par y velocidad
- Se puede almacenar
- Mejor aprovechamiento de la sección de cable para una misma tensión

### Desventajas de la CC

- Como uno usan transformadores no pueden variar la tensión entregada
- Son más difíciles de interrumpir que las alternas
- La circulación de continua bajo tierra corroe galvánicamente lo enterrado


### Ventajas CA monofáfisca

- Transformadores baratos para transportar a grandes distancias con menor costo (alta tensión, baja intensidad) y luego elevarla para el uso en destino
- Facilidad de interrupción

### Desventajas CA monofáfisca

- Fuerte componente alterna del par (inestable para motores)
- No se puede acumular sin ineversor (convertidor a CC)
- No es fácil generar un campo rotatorio
- En los motores de CA no es fácil regular su velocidad de trabajo

### Ventajas CA trifáfisca

- Permite crear un campo rotatorio
- No porducen componente alterna del par
- Los motores trifásicos son más eficientes que mono y bi
- Mejor comportamiento en transformadores

### Desventajas CA trifáfisca

- Se requieren tres cables para la conducción, 4 si se quieren las lineas simples y 5 si se necesita tierra
- Máquinas sincrónicas no se pueden operar muy léjos de la velocidad de sinronismo
- Interruptores tripolares