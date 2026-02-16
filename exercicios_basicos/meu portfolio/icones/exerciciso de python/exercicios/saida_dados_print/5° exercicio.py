# ) Calcular e exibir o IMC (Índice de Massa Corpórea) de uma pessoa de altura (H) em metros e massa
# (M) em quilogramas, sabendo que IMC = M / H2
# .
 # -----------------------------------------------------------------------------------------------------------

M = float(input('informa seu peso  atual:  '))
H =  float(input('informe a sua altura: '))

IMC= M/H**2
print(f' O resultado do indice de massa corporia {IMC:.2F}  KG')