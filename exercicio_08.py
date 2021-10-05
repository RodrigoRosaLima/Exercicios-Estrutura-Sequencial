# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.


print('########## CALCULO DE SALÁRIO ##########')

print()
ganho_hora = float(input('Qual seu sálario por hora? --> '))
horas_mes = int(input('Quantas horas você trabalhou? --> '))
resultado = ganho_hora * horas_mes

print(f'Você trabalhou {horas_mes} horas este mês e irá receber R$ {resultado:.2f}')

