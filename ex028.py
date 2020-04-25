# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usúario tente descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-'*20)
n1 = randint(0, 5)
n2 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)#faz o computador esperar um tempo antes de executar a proxima ação
if n1 == n2:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no {} e não no {}'.format(n1, n2))
