# 2) Escrever um algoritmo em Python que leia a Base (𝐵 > 0) e a Altura (𝐻 > 0) de um retângulo em 
# centímetros e calcule e exiba na tela seu 𝑃𝑒𝑟í𝑚𝑒𝑡𝑟𝑜 (soma dos lados) em: 
# ✓ Centímetros e 
# ✓ Polegadas e  
# ✓ Jardas 
# �
# �𝑙𝑡𝑢𝑟𝑎 (𝐻) 
# Sabendo que: 1 Polegada = 2.54 Centímetros = 0.03 Jardas. 

try:
    perimetroPolegada = 2.54
    jardasPOlegada    = 0.03
    b = float(input('informe o valor da base do retangulo: '))
    h = float(input('informe o valor da altura do retangulo: '))
    if (b <=0 and h<=0 ):
        print('Valor invalido renincie e tente novamente:')
    else:
        perimetro = (2*b + 2*h) 
        Polegadas =  perimetroPolegada / perimetro
        Jardas    =   Polegadas * jardasPOlegada
    print(f'O resultado do perimetro: {perimetro} CM ')
    print(f'O resultado de Polegadas: {Polegadas:.2f} P')
    print(f'O resultado de Jardas:    {Jardas:.2f} J')  
except Exception as e:
    print(f'DADOS INVALIDO {e}')
