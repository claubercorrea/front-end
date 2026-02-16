# 4) Tendo como dado de entrada a altura (h) e o sexo de uma pessoa, construa um algoritmo que calcule 
# seu peso (Massa: Quilogramas) ideal, utilizando as seguintes fórmulas: 
# ✓ Para homens: (72.7 ∗ ℎ) − 58 
# ✓ Para mulheres: (62.1 ∗ ℎ) − 44.7

try:
    print('Escolha uma das opções a baixo: ')
    print('1- opcao: homem')
    print('2- opcao: mulher')
    print('aperte qual quer tecla para poder sair do programa')
    print('\n')
    opcao=  int(input('escolha uma das opções acima: '))
    if(opcao < 1 or opcao >2 ):
        print(' programa encerrado')
    else:    
        h = float(input('informe  a sua altura: ')) 
        if(h <=0):
            print('a informação sobre a altura esta invalida:')
        else:
            if (opcao ==1):
                homem = (72.7*h) -58
                print(f'resultado do IMC para homem: {homem:.2f}')
            else:
                mulher = (62.1*h) -44.7
                print(f'resultado do IMC para mulher: {mulher:.2f}')
except Exception as e:
    print(f'DADOS: INVALIDOS')    
            


    