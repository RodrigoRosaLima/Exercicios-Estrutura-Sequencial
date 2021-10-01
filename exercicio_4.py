# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('=-=' * 5)
print('MÉDIA BIMESTRAL')
print('=-=' * 5)

nota_1 = float(input('Digite a primeira nota: --> '))
nota_2 = float(input('Digite a segunda nota: --> '))
nota_3 = float(input('Digite a terçeira nota: --> '))
nota_4 = float(input('Digite a quarta nota: --> '))

média = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print()
print(f'Sua média foi {média:.2f}')
