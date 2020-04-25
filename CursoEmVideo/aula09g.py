#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = input('Digite seu nome completo: ')
print('Primeiro nome {}'.format(n.split()[0]))
print('Ultimo nome {}'.format(n.split()[n.count("") + 1]))
