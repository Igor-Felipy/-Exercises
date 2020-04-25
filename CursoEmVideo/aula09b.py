#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.
n = input('Digite o seu nome: ')
print(n.upper())
print(n.lower())
print(len(n.replace(' ', '')))
print(n.split()[0])
