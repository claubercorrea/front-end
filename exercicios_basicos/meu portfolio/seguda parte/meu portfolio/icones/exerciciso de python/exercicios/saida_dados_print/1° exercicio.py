# 1) Escreva um algoritmo em Python para cada item a seguir:
# a) Calcular e exibir a hipotenusa (𝐴) de um triângulo retângulo de catetos 𝐵 e 𝐶, sabendo que:
# 𝐴 = √𝐵2 + 𝐶2#
#------------------------------------------------------------------------------------------------#
from logging import exception 
import math 
b = float(input('informe o valor da base: '))
c = float(input('informe o valor o cateto: '))
A = round(math.sqrt(b**2+c**2))
print(f'o resultado da hipotenusa: A={A}')





