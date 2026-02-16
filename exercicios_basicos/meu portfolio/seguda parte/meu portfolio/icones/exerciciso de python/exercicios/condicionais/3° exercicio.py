# 3) Faça um algoritmo em Python que leia o tempo (segundos) de permanência de um aluno no 
# Laboratório de Programação: UVV e exiba na tela seu tempo de permanência: Horas + Minutos 
# + Segundos. Exemplo: Tempo: 10000 Segundos = 2 Hora(s) + 46 Minuto(s) + 40 Segundo(s). 

try:
    tempo = int(input('informe o tempo em minutos: '))

    if(tempo < 0):
        print("horaio inesistente")
    else:
      horas = tempo //3600
      segundos = tempo % 3600
      minutos  =  segundos //60
      segundos%=60   
    print(f'horas: {horas}: minutos: {minutos} : segundos: {segundos}')
except Exception as e:
   print(f'invalido {e}')