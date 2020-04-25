# Escreva um progrsma para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do sálário ou então o empredstimo será negado.

v = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
t = float(input('Em quantos anos deseja pagar o empréstimo? '))
p = v / (t * 12)

print('\nA casa desejada custa R${:.2f}'.format(v))
print('Você escolheu pagar em {:.0f} anos o que daria {:.0f} vezes'.format(t, t*12))
print('Sendo assim você deveria pagar {:.0f} prestações de {:.2f}'.format((t*12), p))
print('Seu valor de crédito maximo é R${:.2f}'.format(s * 30 / 100))
if p <= s * 30 / 100:
    print('Empréstimo autorizado!')
else:
    print('Emprestimo Negado!')
