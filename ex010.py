#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
d = float(input('Quanto você tem na carteira? R$ '))
print('Com R$ {} você pode comprar US${:.2f}!'.format(d, (d/4.25)))
print('Com R$ {} voce pode comprar E${:.2f}'.format(d, (d/4.70)))
print('Com R$ {} voce pode comprar Y${:.2f}'.format(d, (d/0.039)))
