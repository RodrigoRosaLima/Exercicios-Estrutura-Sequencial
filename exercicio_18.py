'''18 - Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos).
'''

print('{:*^30}'.format(' CALCULO DE TEMPO '))
print('-' * 30)

mb = int(input('Qual o tamanho do arquivo em MB que deseja fazer o download? --> '))
link = int(input('Qual a velocidade do seu link em Mbps? --> '))
tempo = (mb / (link / 8)) / 60

print(f'Para efetuar um download de {mb} MB com a velocidade de {link} Mbps, irá demorar {tempo:.0f} minutos.')
