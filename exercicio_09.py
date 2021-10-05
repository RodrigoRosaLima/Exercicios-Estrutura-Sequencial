# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input('Quantos Fahrenheit deseja converter em Graus Celsius? --> '))
resultado = 5 * ((fahrenheit - 32) / 9)

print(f'O valor de {fahrenheit}ºF é equivalente há {resultado:.2f}ºC.')


