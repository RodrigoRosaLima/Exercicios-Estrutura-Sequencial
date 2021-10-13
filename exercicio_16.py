'''16 - Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.'''

import math

print('{:#^30}'.format(' LOJA DE TINTAS '))
print('-' * 30)

area = int(input('Quantos m² deseja pintar? --> '))

cobertura = area / 3
latas = math.ceil(cobertura / 18)
valor = latas * 80

print(f'Para cobrir os {area}m² que deseja, você irá precisar de {latas} latas e irá custar R$ {valor:.2f}')




