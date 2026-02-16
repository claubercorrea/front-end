# 5) Escrever um algoritmo em Python que exiba o público total (inteiro) de um jogo de futebol e 
# forneça a arrecadação (R$: real) do jogo, sabendo que: 
# ✓ Crianças abaixo de 10 anos não pagam; 
# ✓ Jovens de 11 a 17 pagam ½ entrada; 
# ✓ Acima dos 18 anos paga ½ entrada se doarem um quilo de alimento não perecível. 
# ✓ O valor inteiro do ingresso é lido do usuário em reais (R$).
try:
 
    publicoTotal = 0
    soma= 0
    print('escolha uma das opções a baixo:')
    print('1° opções:✓ Crianças abaixo de 10 anos não pagam;')
    print('2° opção:✓ Jovens de 11 a 17 pagam ½ entrada; ')
    print('3° opção:✓ Acima dos 18 anos paga ½ entrada se doarem um quilo de alimento não perecível. ')
    print('aperte qual quer tecla para sair')
    
    opcao = int(input('escolha uma das opções acima: \n'))
    if(opcao < 1 or opcao >4):
        print('programa encerrado ')
    else: 
     ingresso = float(input('informe o valor do ingresso R$: '))
     if(ingresso <=0 or opcao >3):
            print('valor invalido renicie e tente novamente: ')
     else:
        idade =  int(input('infrome a sua idade: '))
        if(idade < 0):
            print(' idade invalidade renicie e tente novamente')
        else:
            if(opcao==1):
                if(idade < 10):
                    print('Crianças abaixo de 10 anos não pagam')
                    ingresso == 0
                    soma+=1
            elif(opcao ==2):
                if(idade  <=17):
                    print('Jovens de 11 a 17 pagam ½ entrada')
                    jovens = ingresso / 2
                    soma+=1
            else:
                if idade >18:
                    print('Acima dos 18 anos paga ½ entrada se doarem um quilo de alimento não perecível')
                    print('sim = dou')
                    print('não= nao dou \n')
                    doacao =input('')
                    if(doacao == 'sim'):
                        ingresso = ingresso / 2
                        soma +=1
                    else:
                        print('pagara o valor total do ingresso ')
                        ingresso =  ingresso
            publicoTotal+=1    
except ValueError:
    print('ERRO DE DADOS')



            
        


