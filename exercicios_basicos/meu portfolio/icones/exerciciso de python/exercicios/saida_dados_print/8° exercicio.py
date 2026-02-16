    # Calcular e exibir a quantidade de tinta (em latas) e o custo (em reais) para pintar um tanque cilíndrico
    # de base circular de Raio (R) e altura (H) em metros, sabendo que:
    # ✓ 1 lata = 5 litros.
    # ✓ 1 litro pinta 3 metros quadrados.
    # ✓ 1 lata custa 50 Reais.

# lata = 5 
# litro = 3 metros
import math
r =  float(input('informe o valor do raio:  '))
h = float(input('informe o valor da altura: '))

area =  2*math.pi(+r+h)

litro = 5 * 3
lata =  math.ceil(area/ litro)
custo= lata *50


print(f'area total a ser pintada { area:.2f} m²')
print(f"quantidade de latas {lata}")
print(f'custo total: R$ {custo:.2f}')   