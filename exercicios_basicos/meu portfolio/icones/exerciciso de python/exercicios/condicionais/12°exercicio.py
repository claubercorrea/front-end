#  Escrever um algoritmo em Python que leia a Massa (Quilos) e a Altura (Metros) do indivíduo 
# calculando o IMC = Massa / Altura2. Após isso, classifique-o conforme a tabela: 
# IMC 
# CLASSIFICAÇÃO 
# <18.5 
# Magreza 
# [18.5, 25[ Saudável 
# [25, 30[ Sobrepeso 
# [30, 35[ Obesidade Grau I 
# [35, 40[ 
# Obesidade Grau II (Severa) 
# >= 40 
# Obesidade Grau III (Mórbida)

try:
    print('\nCalculando o IMC')

    m = float(input('Informe qual e o seu peço atual: '))
    h = float(input('Informe qual e a sua altura: '))

    imc =  m / h

    if( imc < 0):
        print('informação invalida')

    elif(imc < 18.5):
        print('Magreza')
    elif(imc > 18.5 or imc < 25):
        print('Saudável ')
    elif(imc > 25 or imc < 30):
        print('Sobrepeso')
    elif(imc > 30  or imc < 35):
        print('Obesidade Grau I ')
    elif(imc > 35  or imc < 40):
      print('Obesidade Grau II (Severa) ')
    else:
        if(imc >=40):
            print('Obesidade Grau III (Mórbida)')
    print(f' resultado do imc: {imc:.2f} m')
except Exception as e:
    print('ERRO: DADOS INVALIDOS {e}')
  
 

