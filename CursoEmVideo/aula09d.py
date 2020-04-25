#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
n = input('Digite o nome de uma cidade: ')
if n.split()[0] == 'SANTO' or n.split()[0] == 'Santo' or n.split()[0] == 'santo':
    print('Sim o nome começa com SANTO')
else:
    print('Não o nome não começa com SANTO')
