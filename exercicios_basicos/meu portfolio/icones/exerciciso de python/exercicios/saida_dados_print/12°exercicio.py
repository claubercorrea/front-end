# Calcular e exibir a distância máxima (em Quilômetros) de autonomia de um carro que possui um
# tanque de combustível cúbico de lado (L) em metros e Altura (h) de preenchimento do tanque.
# Sabendo que seu consumo é em média 10 km/litro. Sabendo que 1 m3 = 1000 Litro
# ---------------------------------------------------------------------------------
l = float(input('informe o quanto de gasolina tem :'))
h  = float(input('informe a altura do tanque de gasolina:  '))
volume  = l**2*h
litro   = volume *1000
consumo = 10 
autonimia_km=  litro *consumo
print(f'informe quanto de litros esta disponivel: {litro:.2f}')
print(f'informe a autonomia maxima {autonimia_km:.2f}')