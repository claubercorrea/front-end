# c) Calcular e exibir a área de um retângulo de lado (L) e altura (H). Área = L * H
# -----------------------------------------------------------------------------------------------------------

try:
    l = float(input('informe ao valor do lado do retangulo:  '))
    h= float (input('informe o valor da altura do retangulo: '))

    print(f' o resultado do retangulo {round(l*h):2.f}')

except TypeError:
    print('erro de dados')