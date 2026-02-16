# b) Calcular e exibir a área de um quadrado de lado (L). Área = L2
# -----------------------------------------------------------------------------------------------------------


try:
     l = int(input('informe o valor da area: '))
     print(f' o resultado do valor da area: {l**2}')
except Exception as e:
     print(f'erro de dados {e}')