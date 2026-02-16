#  Escrever um algoritmo em Python que determine o volume e a área de uma esfera de raio 𝑟 (∈ ℝ+∗).  
# Sendo que 𝜋 = 3.14. 
# ✓ 𝐴𝑟𝑒𝑎 =4∗ 𝜋∗ 𝑟2 
# ✓ 𝑉𝑜𝑙𝑢𝑚𝑒 =4
# 3
# ∗ 𝜋∗𝑟3 


import math
try:
    R = float(input('Informe o valo do raio: '))
    if R <= 0:
        print('valor invalido. renicie tenten novamente')
    else:

        area = round(4 * math.pi * R**2)
        volume = round((4/3) * math.pi *R**3)
    print(f'O resultado da area: {area:.2f} M² ')
    print(f'O resultado do volume: {volume:.2f} M³ ')


    
except Exception as e:
    print(f'ERRO DE DADOS {e}')