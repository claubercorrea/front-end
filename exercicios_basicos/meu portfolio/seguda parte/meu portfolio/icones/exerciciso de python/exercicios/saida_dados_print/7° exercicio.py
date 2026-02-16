# g) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
# mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato. Com isso, exiba na tela:
# ✓ salário bruto.
# ✓ quanto pagou ao INSS.'
# ✓ quanto pagou ao sindicato.
# ✓ o salário líquido = Brutos - Descontos.    
# -----------------------------------------------------------------------------------------------------------

salarioBruto = float('informe o seu salario bruto:  ')
bruto = salarioBruto * 0.11
imposto      = salarioBruto * 0.08
INSS         =  salarioBruto  * 0.05

salario_liquido =  bruto - imposto - INSS

print(f'o resultado do salario liquido: R$ {salario_liquido:.2f}')
