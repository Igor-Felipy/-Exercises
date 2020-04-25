# Crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e raiz quadrada.
n = int(input('digite um numero: '))
print('O dobro é: {}! o triplo é: {}! e a raiz quadrada é: {:.5f}'.format(n * 2, n * 3, n**(1/2)))