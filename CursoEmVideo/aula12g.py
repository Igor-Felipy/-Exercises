#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - 9 anos: mirim - 14 ano: infantil - 19 anos: junior - 20 anos: senior - acima: master
import datetime
i = int(input('Qual seu ano de nascimento? '))
a = datetime.date.today().year

if a - i <= 9:
    print('MIRIM')
elif a - i <= 14:
    print('INFANTIL')
elif a - i <= 19:
    print('JUNIOR')
elif a - i <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
