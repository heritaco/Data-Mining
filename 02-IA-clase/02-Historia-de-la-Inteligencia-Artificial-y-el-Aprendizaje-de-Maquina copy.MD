<link rel="stylesheet" type="text/css" href="styles.css">
<link rel="stylesheet" href="github-markdown.css">
<script src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
<div class="container">


<div class="header">
  <h1>Historia de la Inteligencia Artificial y el Aprendizaje de Máquina</h1>
  <h3>P25 LDS1021 1: Minería de Datos</h3>
  <p>22 de Enero de 2025</p>
</div>



  <div class="bubble right">
¿Qué son transistores? 


  </div class="bubble right">
  <div class="bubble left">

 
Un **transistor** es un componente electrónico que funciona como un interruptor o un amplificador de señales eléctricas. Es uno de los elementos fundamentales de la electrónica moderna y se utiliza en casi todos los dispositivos electrónicos, desde teléfonos celulares hasta computadoras.



  </div class="bubble left">
  <div class="bubble left">

 Principales funciones del transistor:
1. **Interruptor:** Puede encender o apagar el flujo de corriente eléctrica en un circuito.
2. **Amplificador:** Puede aumentar la potencia de una señal eléctrica débil para hacerla más fuerte.




  </div class="bubble left">
  <div class="bubble left">


Los transistores son la base de los circuitos integrados y permiten construir computadoras y otros dispositivos digitales. Al miniaturizarlos, los ingenieros han podido desarrollar chips con millones de transistores, lo que ha impulsado el avance tecnológico desde mediados del siglo XX.

¿Te interesa saber más sobre su funcionamiento o aplicaciones específicas?








  </div class="bubble left">

  <div class="bubble right">
O sea ¿es un switch con pesos?


  </div class="bubble right">

  <div class="bubble left">

 
¡Exactamente! Un **transistor** es como un *switch* (interruptor) que puede ser controlado. La diferencia clave es que este *switch* no solo tiene estados de encendido (*on*) y apagado (*off*), sino que también puede actuar como un regulador (en el caso de los amplificadores) dependiendo de cuánto "peso" o señal le des para controlarlo.

En términos de "pesos," si piensas en aplicaciones como **inteligencia artificial o redes neuronales**, los transistores en los circuitos pueden representar cómo se ajustan o "pesan" las señales para procesar información, como si fueran las sinapsis de un cerebro artificial.  







  </div class="bubble left">

  <div class="bubble right">
  ¿Qué es un perceptrón? 


  </div class="bubble right">

  <div class="bubble left">

Un **perceptrón** es el modelo más básico de una **red neuronal artificial**, diseñado para simular cómo las neuronas humanas procesan información. Fue introducido en 1958 por Frank Rosenblatt y es una de las primeras ideas que dieron forma a lo que hoy conocemos como inteligencia artificial.



  </div class="bubble left">
  <div class="bubble left">

 ¿Cómo funciona un perceptrón?

Un perceptrón toma varias **entradas** (inputs), las procesa a través de un conjunto de **pesos** y luego genera una **salida** (output). 



  </div class="bubble left">
  <div class="bubble left">

**Pasos básicos:**
1. **Entradas ($x_1, x_2, \dots, x_n$):**
   Son los valores de entrada (por ejemplo, datos numéricos).
   
2. **Pesos ($w_1, w_2, \dots, w_n$):**
   Cada entrada tiene un peso asociado que indica su importancia en el modelo. Estos pesos son ajustables durante el entrenamiento.

3. **Combinación lineal:**
   Se calcula una suma ponderada de las entradas y los pesos:
   $$
   z = \sum_{i=1}^{n} w_i \cdot x_i + b
   $$
   Aquí, $b$ es el **sesgo** (*bias*), un término adicional que ayuda a ajustar el modelo.

4. **Función de activación:**
   El resultado de la combinación lineal pasa por una función de activación que decide si la salida será **1 (activo)** o **0 (inactivo)**, según un umbral. Por ejemplo:
   $$
   \text{Salida} = 
   \begin{cases} 
   1 & \text{si } z \geq \text{umbral} \\ 
   0 & \text{si } z < \text{umbral} 
   \end{cases}
   $$



  </div class="bubble left">
  <div class="bubble left">

**Representación gráfica:**

Un perceptrón es como una "neurona" con múltiples entradas, pesos que ajustan esas entradas, y una salida que depende de cómo interactúan las entradas y los pesos.



  </div class="bubble left">
  <div class="bubble left">

 ¿Para qué sirve?
Un perceptrón puede usarse para **clasificar datos** en dos categorías (como 0 o 1, sí o no, verdadero o falso). Por ejemplo:
- Clasificar si un correo es spam o no.
- Determinar si una imagen contiene un gato o no.



  </div class="bubble left">
  <div class="bubble left">

 Limitaciones:
El perceptrón solo puede resolver problemas que son **linealmente separables**. Esto significa que si los datos no se pueden separar con una línea recta (en 2D) o un plano (en 3D), el perceptrón no puede clasificarlos correctamente.





  </div class="bubble left">

  <div class="bubble right">
un perceptron se hace con un transistor? 


  </div class="bubble right">

  <div class="bubble left">

 No directamente, pero un **perceptrón** se puede construir de manera abstracta usando circuitos electrónicos, y los **transistores** son los bloques fundamentales de esos circuitos. Déjame explicarlo mejor:

1. **Transistores en hardware:**
   - Un transistor funciona como un interruptor o regulador, y puede ser usado para implementar operaciones matemáticas básicas, como sumas y multiplicaciones.
   - Los perceptrones requieren realizar operaciones como **suma ponderada** ($\sum w_i \cdot x_i$) y aplicar funciones lógicas (activaciones). Esto se puede implementar físicamente usando **circuitos electrónicos** hechos de transistores.

2. **Cómo encajan los transistores en un perceptrón:**
   - **Pesos:** Los pesos ($w_i$) pueden ser representados por valores ajustables en el circuito, como resistencias o configuraciones de transistores.
   - **Suma:** La combinación lineal ($\sum w_i \cdot x_i + b$) puede ser implementada con circuitos sumadores construidos con transistores.
   - **Activación:** Una función de activación (por ejemplo, una función escalón) puede ser simulada con un diseño que activa o desactiva una salida según el voltaje (nivel de señal).

3. **Implementación práctica:**
   - Aunque conceptualmente un perceptrón podría construirse directamente con transistores, en la práctica se implementa en software o hardware especializado, como procesadores, **chips ASIC** (circuitos integrados específicos) o **GPUs**, que están hechos de millones o incluso miles de millones de transistores.
   - En el pasado, los **perceptrones físicos** sí se construyeron con circuitos electrónicos simples, usando relés y transistores. Hoy en día, los perceptrones se simulan en computadoras digitales.

En resumen, un perceptrón no es un transistor en sí, pero los transistores pueden ser usados para construir el hardware que lo simula o ejecuta. ¿Te interesa saber más sobre cómo esto se aplica a hardware moderno como GPUs o chips de inteligencia artificial?



  </div class="bubble left">

  <div class="bubble right">
que es back-propagation? 


  </div class="bubble right">

  <div class="bubble left">

**Backpropagation** (abreviatura de *backward propagation of errors*) es un algoritmo utilizado en el entrenamiento de **redes neuronales artificiales**. Su principal objetivo es ajustar los **pesos** de la red para minimizar el error en las predicciones. Es una técnica clave en el aprendizaje profundo (**deep learning**) y está basada en el cálculo del gradiente para optimizar los parámetros del modelo.



  </div class="bubble left">
  <div class="bubble left">

 ¿Cómo funciona el backpropagation?
El algoritmo trabaja en dos pasos principales: **propagación hacia adelante (forward pass)** y **propagación hacia atrás (backward pass)**.

1. **Propagación hacia adelante:**
   - Los datos de entrada pasan a través de la red neuronal, capa por capa, hasta llegar a la salida.
   - La salida de la red se compara con los valores reales (etiquetas o *ground truth*), y se calcula un **error** usando una función de pérdida (como el error cuadrático medio o la entropía cruzada).

2. **Propagación hacia atrás:**
   - El error calculado se propaga desde la salida hacia las capas anteriores, de forma "reversa".
   - Utilizando el **cálculo del gradiente**, se determina cómo cada peso de la red contribuye al error.
   - Luego, los pesos de la red se ajustan en función de estos gradientes para reducir el error.

Este proceso se repite iterativamente para que la red aprenda a hacer mejores predicciones.



  </div class="bubble left">
  <div class="bubble left">

 Conceptos clave en backpropagation:
1. **Función de pérdida:** 
   - Mide el error entre la salida de la red y el valor real. Ejemplos: 
     - Error cuadrático medio (MSE).
     - Entropía cruzada.

2. **Gradiente:**
   - Es la derivada parcial de la función de pérdida con respecto a los pesos de la red. Se utiliza para determinar la dirección en la que se deben ajustar los pesos para reducir el error.

3. **Regla de actualización:**
   - Los pesos se actualizan usando un optimizador, como el **descenso de gradiente**, con la fórmula:
     $$
     w = w - \eta \cdot \frac{\partial L}{\partial w}
     $$
     Donde:
     - $w$ es un peso.
     - $\eta$ es la tasa de aprendizaje (*learning rate*).
     - $\frac{\partial L}{\partial w}$ es el gradiente de la función de pérdida.




  </div class="bubble left">
  <div class="bubble left">

 ¿Por qué es importante?
Backpropagation es fundamental porque:
- Permite entrenar redes neuronales profundas con múltiples capas.
- Es eficiente en términos computacionales, especialmente cuando se combina con optimizadores como el **descenso de gradiente estocástico (SGD)**.
- Es la base de la mayoría de los avances en aprendizaje profundo.

¿Te gustaría un ejemplo paso a paso o algún caso práctico para entenderlo mejor?








  </div class="bubble left">

  <div class="bubble right">
mmm explicamelo en corto


  </div class="bubble right">

  <div class="bubble left">

 
Backpropagation es el algoritmo que permite entrenar redes neuronales ajustando los pesos para minimizar el error. Funciona en dos pasos:

Propagación hacia adelante: La entrada pasa por la red y se calcula el error comparando la salida con el valor real.
Propagación hacia atrás: El error se distribuye de forma inversa por la red, usando cálculo de gradientes para ajustar los pesos y reducir el error.
Se repite este proceso hasta que la red aprende a predecir con precisión. Es como enseñarle a la red a corregir sus errores paso a paso.




</div class="container">