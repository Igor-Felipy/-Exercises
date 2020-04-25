#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
ht = ((ca**2) + (co**2))**(1/2)
print(ht)
