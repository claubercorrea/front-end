# 7)a) Escrever um algoritmo em Python que leia o Preço de uma mercadoria e exiba o preço na tela 
# reajustado de 3%. O usuário escolherá a Opção: “Acréscimo” ou “Desconto” para o reajuste de 3 %. 
# b. Faça agora o mesmo exercício, entretanto; lendo o reajuste (em %) do usuário.
try:
    print('MENU\n')
    print('1° opcao: desconto ')
    print('2° opcao: acrescimo ')
    print('qual quer tecla para sair do programa \n')
    desconto = 3    
    acrescimo = 3
    soma = 0
    opcao = int(input('escolha uma das opcoes acima: '))

    if(opcao < 1 or opcao >2):
        print('opcao invalida recinicie  e tente novamente: ')
    else:
        mercadoria = float(input('informe o valor do produto: '))
        if(mercadoria <=0):
            print('valor invalido')
        else:
            if(opcao ==1):
                descontoMercadoria = (desconto /mercadoria) *100
                soma+=1
                print(f'desconto da mercadoria {descontoMercadoria:.1f} %')
            else:
                acrecimoProduto = (acrescimo /mercadoria) *100
                soma+=1
                print(f'acrescimo da mercadoria {acrecimoProduto:.1f} %')
            
except ValueError:
    print('dados invalido')

