#Crie um programa que leia o nome de uma pessoa e diga se ela te "SILVA" no nome
n = input('Digite o seu nome: ')
if 'SILVA' in n or 'Silva' in n or 'silva' in n:
    print('Você tem SILVA no nome!')
else:
    print('Você não tem silva no nome!')
