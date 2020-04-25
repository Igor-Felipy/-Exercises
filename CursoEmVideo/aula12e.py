# Faça um programa que leia o ano de nascimento de um jovem e informe,  de acordo com sua idade: - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - se já passou do tempo do alistamento.
# Seu programa deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
a = int(input('Digite o seu ano de nascimento: '))
b = datetime.date.today().year
c = b - a
if b - a < 18:
    print('Você ainda vai se alistar')
    print('Faltam {} anos para você'.format(18-c))
elif b - a > 18:
    print('Você ja deveria ter se alistado')
    print('Já se passaram {} anos'.format(c-18))
elif b - a == 18:
    print('Você deve se alistar ainda esse ano!')