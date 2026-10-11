### `informe.md` (Respuestas a la sección 6 de la rúbrica)

# informe de convergencia
## 1. metodo con menos iteraciones por funcion
en funciones con raices simples y derivadas bien condicionadas, newton-raphson y newton-raphson mejorado alcanzaron la tolerancia en la menor cantidad de iteraciones (2 a 3 iteraciones en promedio). esto ocurre por su orden de convergencia cuadratico. la secante requirio entre 3 y 4 iteraciones (orden superlineal). biseccion fue el metodo mas lento en todas (entre 19 y 20 iteraciones) dado que reduce el intervalo a la mitad en cada paso sin considerar la pendiente ni el valor de f(x).

## 2. orden de convergencia y reflejo en grafico |error| vs iteracion
- biseccion: orden lineal (razon 1/2). en la grafica logaritmica se observa como una recta descendente constante y uniforme.
- falsa posicion: orden lineal. en funciones asimetricas suele retener un extremo fijo, ralentizando su recta de decrecimiento respecto a los abiertos.
- secante: orden superlineal (aprox 1.618). presenta una curva concava hacia abajo con caida pronunciada al acercarse a la raiz.
- newton-raphson y newton mejorado: orden cuadratico (en raices simples). la caida del error en escala logaritmica es casi vertical en las ultimas iteraciones.

## 3. metodos que requieren cambio de signo
- metodos cerrados: biseccion y falsa posicion exigen f(a) * f(b) < 0 para garantizar existencia por el teorema de bolzano.
- metodos abiertos: punto fijo, secante, newton-raphson y newton mejorado no requieren cambio de signo; parten de aproximaciones puntuales x0 (o x0, x1).

## 4. comportamiento en raiz doble f(x) = (x - 2)^2
- biseccion y falsa posicion no aplican porque f(x) >= 0 en todo el dominio; no existe intervalo con cambio de signo.
- newton-raphson clasico pierde su orden cuadratico y se vuelve lineal con razon 1/2 debido a que f'(2) = 0. requirio 10 iteraciones para alcanzar la tolerancia.
- newton mejorado se comporta de forma optima: converge en 1 sola iteracion a la raiz exacta x = 2.0 al compensar la multiplicidad con el denominador (f')^2 - f*f''.

## 5. influencia del intervalo y estimacion inicial
en los metodos cerrados, un intervalo mas amplio incrementa el numero de iteraciones requeridas por biseccion (segun la formula ceil(log2((b-a)/tol))). en los metodos abiertos, si x0 se aleja o se ubica cerca de un punto donde la derivada es nula o el punto fijo tiene |g'(x)| > 1, el metodo puede divergir o ciclarse.

## 6. recomendacion segun tipo de funcion
- para funciones donde se conoce la derivada analitica y se busca rapidez: newton-raphson en raiz simple y newton mejorado en raices multiples.
- si la derivada es computacionalmente costosa de evaluar: secante.
- si la funcion presenta discontinuidades o derivadas mal condicionadas y se cuenta con un cambio de signo: biseccion por ser incondicionalmente robusto.

## conclusion
la comparacion evidencia el compromiso entre velocidad de convergencia y robustez de aplicacion. los metodos abiertos de segundo orden minimizan el costo computacional cuando las condiciones locales se cumplen, mientras que los metodos cerrados garantizan convergencia a costa de un avance lineal. en raices con multiplicidad superior a uno, la formulacion modificada de newton restaura la tasa cuadratica que los otros metodos pierden.