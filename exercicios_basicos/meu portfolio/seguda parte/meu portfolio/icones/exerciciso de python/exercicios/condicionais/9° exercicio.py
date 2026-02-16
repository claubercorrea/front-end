# 9) Escrever um algoritmo em Python que determine a conversão entre as moedas: Real, Dólar e Libra, 
# de uma determinada quantidade em espécie e moeda informadas pelo usuário, sabendo que:                                        
# R$ 4.08 = US$ 1.12 = £ 1.0 (Ver no Google a Cotação do "dia") 

try:
    TAXA_R = 4.80
    TAXA_D = 1.12
    TAXA_L = 1.00
    
    VALOR_LIBRAS     = 0.0
    RESUTALDO_R      = 0.0
    RESUTALDO_D      = 0.0
    RESUTALDO_L      = 0.0

    moedaOrigem      =  input('Informe a moeda de origem (R/D/L):')
    print('---Converso de comoedas: Real (R), Dólar (D), Libra(L)--- '.upper() )
    print('')
    quantidade =  float(input('Informe a quantidade em espécie e ser convertido: '))

    if (moedaOrigem == 'R'):
        VALOR_LIBRAS =  quantidade /TAXA_R
        
        RESUTALDO_R =  quantidade
        RESUTALDO_D =  VALOR_LIBRAS / TAXA_D
        RESUTALDO_L =  VALOR_LIBRAS /TAXA_L
    elif(moedaOrigem =='D'):
        VALOR_LIBRAS = quantidade /TAXA_D

        RESUTALDO_R =  VALOR_LIBRAS*TAXA_R
        RESUTALDO_D =  quantidade
        RESUTALDO_L = VALOR_LIBRAS * TAXA_L
    elif(moedaOrigem =="L"):
        VALOR_LIBRAS = quantidade

        RESUTALDO_R = VALOR_LIBRAS * TAXA_R
        RESUTALDO_D = VALOR_LIBRAS * TAXA_D
        RESUTALDO_L = quantidade
    else:
        print('\nERRO: Moeda de origem invalido. Digite R, D OU L.') 
    if(moedaOrigem in ('R','D','L')):
        print(f'\n---Resultado da conversão  para  {quantidade:,.2f} {moedaOrigem}')
    if(moedaOrigem !='R'):
          print(f' -> R$ {RESUTALDO_R:.2f} (REAIS)')
    if(moedaOrigem !='D'):
        print(f' -> US$ {RESUTALDO_D:.2f} (DÓLAR)')
    if(moedaOrigem !='R'):
        print(f' -> £ {RESUTALDO_L:.2f} (LIBRA)')
    print('---------------------------------------------------------------------------------------')
except Exception as e:
    print(f'ERRO: DADOS INVALIDADOS')  