#Escreva umprograma que faça o computador "pensar" em um numero de 0 a 5 e peça para o usuario tentar descobrir qual foi o escolhido pelo computador
#O programa deverá escrever na tela se o usuàrio venceu ou perdeu.

import random

n = random.randint(0, 5)
m = int(input('Digite o numero ecolhido por mim O grande computador!'))
if m == n:
    print('Voce acertou que magnifico!')
else:
    print('Você errou mente fraca!')
