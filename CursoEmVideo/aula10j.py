#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu qumento.
#Para salarios superiores a R$1250.00, calcule um aumento de 10%.
#Para inferiores ou iguais, o aumento é de 15%
s = float(input('Digite o salario do funcionario: '))

if s > 1250.00 :
    print('Esse funcionario tem direito a 10% de aumento!')
    print('O salario de {} vai passar para {:.2f}!'.format(s, s*1.10))
else:
    print('Esse funcionario tem direito a 15% de aumento!')
    print('O salario de {} vai passar para {:.2f}!'.format(s, s*1.15))
