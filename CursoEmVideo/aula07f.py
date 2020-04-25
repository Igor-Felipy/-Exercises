# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um numero para que seja calculada a sua tabuada: '))
con = int(input('Digite ate que numero sera contada a tabuada: '))
co = 0
while co <= con:
    print('{} X {} = {}'.format(n, co, (co*n)))
    co +=1

