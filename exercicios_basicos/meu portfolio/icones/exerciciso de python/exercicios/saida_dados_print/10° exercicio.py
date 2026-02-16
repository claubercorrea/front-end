# j) Calcular e exibir o tempo (em horas) de autonomia de uma caixa d’água de um restaurante que
# consome 1350 litros por hora em média. O tanque do restaurante é cilíndrico de base circular de Raio
# (R) e de altura (H) em metros. Sabendo que 1 m3 = 1000 Litros.
import math 

r = float(input('informe o valor do raio: '))
h  = float(input('informe o valor da altura: '))

volume =  math.pi.r**2*h
volume_litro = volume*1000
consumo = 1350
horas =  volume_litro/1350
print(f'o voliume do taque: {volume:.2f} m²')
print(f'volume_tanque: {volume_litro:.2f} litro')
print(f'autonomia do sistema: {horas:.2f}')