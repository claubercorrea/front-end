# Escrever um algoritmo em Python que leia uma temperatura em Celsius (C) ou Fahrenheit (F) e faça 
# a conversão entre as unidades. Considere que o usuário informe: 
# ✓ Escala de entrada: Celsius ou Fahrenheit; 
# ✓ Valor da temperatura; 
# ✓ Sendo a fórmula de conversão: 𝐶
# 5
# = 𝐹−32
try:
    print('MENU')
    print('\nEscolha uma das opções abaixo: ')
    print('1°opção:1-CELSIOS ')
    print('2°opção:2-Fahrenheit ')
    print('clique em qualquer tecla para sair: ')
    opcao = int(input('Escolha uma das opções acima:'))
    if(opcao < 1 or opcao >2):
        print('opcao invalida renicie e tente novamente:')
    else:
       C =  float(input('informe o quantos graus: '))
       F =  float(input('informe quantos graus:  '))

    if(opcao ==1):
        c = (F-32) * (5/9)
        print(f'resuldo em celsios: {c:.2f} °')
    else:
  
        f = (9/5) * (C + 32)

        print(f'resultado de Fahrenheit: {f:.2f} °')
    
except Exception as e:
    print(f'ERRO: DADOS INVALIDOS')    
    