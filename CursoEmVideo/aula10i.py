#Façaum programa que leia tres numeros e mostre qual é maior e qual é menor.
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('O numero {} é o maior de todos!'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O numero {} é o maior de todos!'.format(n2))
else:
    print('O numero {} é o maior de todos!'.format(n3))

if n1 < n2 and n1 < n3:
    print('O numero {} é o menor de todos!'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O numero {} é o menor de toddos!'.format(n2))
else:
    print('O numero {} é o menor de todos!'.format(n3))
