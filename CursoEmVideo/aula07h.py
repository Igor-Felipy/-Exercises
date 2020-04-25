# Faça um program que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m.
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
print('A área da parede é de {}m2! e você precisara de {} litros de tinta para pintar a parede!'.format(area, area/2))