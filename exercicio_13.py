'''13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
O programa pede o sexo, altura e peso de hoje e mostra para a pessoa qual o peso ideal e quanto ela precisa perder ou ganhar.
'''

print('{:#^30}'.format(' PESO IDEAL '))

sexo = input('De qual sexo deseja saber o peso idal? h/m: --> ')

if sexo == 'h':
    altura_homem = float(input('Qual a altura? --> '))
    peso_hoje = float(input('Qua seu peso hoje? --> '))
    resultado_homem = (72.7 * altura_homem) - 58
    perca_h = resultado_homem - peso_hoje
    if peso_hoje > resultado_homem:
        print(f'O seu peso hoje é {peso_hoje}kg e seu peso ideal é {resultado_homem:.3f}kg, você precisa perder {perca_h:.3f}kg.')
    else:
        print(f'O seu peso hoje é {peso_hoje}kg e seu peso ideal é {resultado_homem:.3f}kg, você precisa ganhar {perca_h:.3f}kg.')
else:
    altura_mulher = float(input('Qual a altura? --> '))
    peso_hoje_m = float(input('Qua seu peso hoje? --> '))
    resultado_mulher = (62.1 * altura_mulher) - 44.7
    perca_m = resultado_mulher - peso_hoje_m
    if peso_hoje_m > resultado_mulher:
        print(f'O seu peso hoje é {peso_hoje_m}kg e seu peso ideal é {resultado_mulher:.3f}kg, você precisa perder {perca_m:.3f}kg.')
    else:
        print(f'O seu peso hoje é {peso_hoje_m}kg e seu peso ideal é {resultado_mulher:.3f}kg, você precisa ganhar {perca_m:.3f}kg.')
