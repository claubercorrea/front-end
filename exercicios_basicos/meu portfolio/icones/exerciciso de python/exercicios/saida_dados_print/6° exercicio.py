# f) Calcular e exibir o volume em litros de uma esfera de Raio (R), sabendo que o usuário deve informar
# o Raio (R) em metros. Sabe-se que: 𝑉𝑜𝑙𝑢𝑚𝑒𝐸𝑠𝑓𝑒𝑟𝑎 = 4/3 * π * R3
# e que 1 Litro é igual a 10-3 m3
# -----------------------------------------------------------------------------------------------------------

import math
R = float(input('informe o valor do número do raio: '))
volumeEsfera = (4/3) * math.pi*R**2
print(f'o resultado do volume de Esfera {volumeEsfera:.2f}')