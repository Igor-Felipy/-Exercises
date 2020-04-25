#Deseenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('As retas podem sim formar um triângulo!')
else:
    print('As reta não podem formar um triângulo!')
