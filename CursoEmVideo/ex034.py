# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento 15%.
s = float(input('Qual é o salário do funcionário? R$'))
if s <= 1250:
    sa = s + (s*0.15)
else:
    sa = s + (s * 0.1)
print('Quem ganhava R${} passa a ganhar R${}'.format(s, sa))
