from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('O valor da hipotenusa é: {:.2f}'.format(hypot(ca, co)))
#print('O valor da hipotenusa é: {:.2f}'.format(((co**2) + (ca**2)) ** (1/2)))
