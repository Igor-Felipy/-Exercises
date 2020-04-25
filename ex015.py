#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado  e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
d = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
print('O total a pagar é de R${:.2f}'.format((d * 60.0)+(km * 0.15)))
