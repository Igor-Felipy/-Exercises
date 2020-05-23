import random
a1 = input('primeiro aluno:')
a2 = input('Segundo alluno:')
a3 = input('terceiro aluno:')
a4 = input('quarto aluno:')
lista = [a1, a2, a3, a4]
r = random.choice(lista)
print('O aluno escolhido foi: {}'.format(r))
