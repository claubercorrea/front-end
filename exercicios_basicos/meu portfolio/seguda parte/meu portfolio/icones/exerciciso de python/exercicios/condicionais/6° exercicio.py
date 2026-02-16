# 6) Faça um algoritmo que leia um número positivo e exiba se seu quadrado é ímpar e múltiplo de 11.

try:
    numero = int(input('informe um numero possitivo: '))
    if(numero < 0 ):
        print('numero invalido pois, o numero precisa ser um numero positivo renicie te tente novamente: ')
    else:
        quadrado = numero **2
        if (quadrado %11 ==0):
            print('sao numeros impares multiplos de 11')
        else:
            print( 'invalido')
except Exception as e:
    print('erro de dados')


   