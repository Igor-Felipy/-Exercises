# Faça um algoritmo que leia o salário de um funcionario e mostre o seu novo salário, com 15% de aumento.
s = float(input('Qual é o salario do funcionario? R$'))
print('Um funcionário que ganhava R${}, com 15% de aumento vai passar a ganhar R${:.2f}'.format(s,s + (s*15/100)))
