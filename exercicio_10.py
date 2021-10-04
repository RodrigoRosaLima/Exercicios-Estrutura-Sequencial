# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (c * 1.8) + 32

celsius = float(input('Quantos graus Celsius deseja transformar em graus Fahrenheit? --> '))
resultado = (celsius * 1.8) + 32

print(f'O valor de {celsius}ºC é equivalente há {resultado:.2f}ºF.')

