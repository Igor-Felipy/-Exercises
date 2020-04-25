#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "a".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

f = input('Digite uma frase: ')
print('A letra a aparece {} vezes.'.format(f.count('a') + f.count('A')))
print('A letra a aparece pela primeira vez na posição {}'.format(f.find('a')))
print('A letra a aparece pela ultima vez na posição {}'.format(f.rfind('a')))
