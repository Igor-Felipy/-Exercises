# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''
m = int(input('Digite um numero: '))
print('='*20)
print('tabuada do {}\n {} X  1  = {}\n {} X  2 = {}\n {} X  3 = {}\n {} X  4 = {}\n {} X  5 = {}\n {} X  6 = {}\n {} X  7 = {}\n {} X  8 = {}\n {} X  9 = {}\n {} X 10 = {}'.format(m, m, (m*1), m, (m*2), m, (m*3), m, (m*4), m, (m*5), m, (m*6), m, (m*7), m, (m*8), m, (m*9), m, (m*10)))
print('='*20)
'''
# Versão com laço
m = int(input('Digite um numero: '))
n = int(input('Digite o maximo da tabuada: '))
g = 0

print('='*20)

while g <= n:
    print('{} X {} = {}'.format(m, g, (m*g)))
    g += 1

print('='*20)
