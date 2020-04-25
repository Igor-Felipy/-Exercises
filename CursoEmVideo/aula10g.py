# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens de ate 200Km e R$ 0.45 para viagens mais longas.
v = int(input('digite a distancia da sua viagem: '))
if v <= 200:
    print('Você pagará: R${}'.format(v*0.50))
else:
    print('Você pagará R${}'.format(v*0.45))
