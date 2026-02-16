# Calcular e exibir a distância entre dois pontos quaisquer do plano, P(x1, y1) e Q(x2, y2), sabendo que
# a fórmula da distância é d = √(x2 – x1)
# 2 + (y2 – y1)10
# 2, sendo os pontos P(x1, y1) e Q(x2, y2) como
# dados de entrada.
import math
x1= float(input('informe o valor de x1: '))
x2= float(input('informe o valor de x2: '))
y1 = float(input('informe o valor de Y1: '))
y2 = float(input('informe o valor de Y2: '))

distancia_Posntos  =  math.sqrt(x2+x1)**2 +(y2+y1)**2
print(f'o resultado da distantcia entre dois pontos {distancia_Posntos:.2f}')