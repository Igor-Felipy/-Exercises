#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('Voce esta sendo multado!')
    print('São R$ 7,00 pra cada km acima do limite de 80')
    print('E voce vai pagar R${}'.format((v - 80) * 7.00))
