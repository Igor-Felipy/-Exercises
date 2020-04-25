#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
esc = random.randint(1, 4)
print('O escolhido foi: ')
if esc == 1:
    print(a1)
if esc == 2:
    print(a2)
if esc == 3:
    print(a3)
if esc == 4:
    print(a4)
