# k) Faça um programa que peça o tamanho de um arquivo para download (em Megabytes) e a
# velocidade de um link de Internet (em Megabytes / Segundo), calcule e informe o tempo: Minutos +
# Segundos aproximado de download do arquivo usando este link.


tempo = float(input('informe o tempo:  '))
tamanho=  float(input('informe quantos mega bits: '))
tempo_segundos = tamanho / tempo
segundos = int(round(tempo_segundos //60))
minutos  = int(round(tempo_segundos % 60))
print(f'tempo aproximado do downlond: {minutos} minuntos e  {segundos }')
