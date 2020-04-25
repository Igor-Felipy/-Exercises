# nome = input('Qual seu nome? ')
# print('Prazer em te conhecer {:=>20}!'.format(nome))
# print('Prazer em te conhecer {:=<20}!'.format(nome))
# print('Prazer em te conhecer {:=^20}!'.format(nome))


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}'.format(n1 + n2))
print('A multiplacação é {} e a divisão é {:.3f} '.format(m, d), end='')
print('A divisão inteira é {} e a potencia é {}'.format(di, e))
