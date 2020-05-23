# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
print('Sua paredeta a dimensão de {}X{} e sua área é de {}.'.format(l, a, area))
print('Para pintar essa parede, você precisará de {:.3f}l de tinta.'.format(area/2))
