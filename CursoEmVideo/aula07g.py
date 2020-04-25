# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólare ela pode comprar.
#Considere US$1,00 = R$3,27
d = float(input('Quanto você tem na carteira? '))
print('Com essa quantia você pode comprar {:.2f} de Dólar'.format(d/4.28))