#Desenvolva um programa que leia 3 retas e diga se elas podem formar um triangulo.
a1 = float(input('Digite o valor da primeira reta: '))
a2 = float(input('Digite o valor da segunda reta: '))
a3 = float(input('Digite o valor da terceira reta: '))

if (a1-a2) < a3 and (a1-a2) < a1+a3 or (a1-a3) < a2 and (a1-a3) < a1+a3 or (a2-a3)<a1 and (a2-a3)< a2-a3:
    print('Essas retas podem sim formar um triangulo!')
else:
    print('Essas retas não podem formar um triangulo!')
