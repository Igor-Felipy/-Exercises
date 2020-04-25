#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: -1 para binário -2 para octal -3 para hexadecimal
import bhdoconvert
n = int(input('Entre com um número inteiro qualquer: '))
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
c = int(input('Escolha a base de conversão:'))


if c == 1:
    print('Base decimal: {} \nBase Binária {}'.format(n, bhdoconvert.decBin(n)))
elif c == 2:
    print('Base decimal: {} \nBase Octal: {}'.format(n, bhdoconvert.decOct(n)))
elif c == 3:
    print('Base decimal: {} \nBase Hexadecimal: {}'.format(n, bhdoconvert.decHex(n)))
else:
    print('ERRO!!!!!!!!!')
