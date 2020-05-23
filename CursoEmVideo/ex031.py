#Desenvolva um programa que pergunte a distnciâde uma viagem em km. Calcule o preço da passagem, cobrando R$00,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
d = int(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}KM.'.format(d))
if d <=200 :
    print('E o preço da sua passagem será de R${}'.format(d*0.50))
else:
    print('E o preço da sua passagem será de RS{}'.format(d*0.45))
