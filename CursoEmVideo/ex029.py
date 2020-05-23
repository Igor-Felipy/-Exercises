# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite
v = int(input('Qual a  velocidade atual do carro?'))

if v <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de RS{}!'.format((v-80)*7.00))
