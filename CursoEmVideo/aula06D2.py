#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
n1 = input('Digite um algo: ')
print(n1, ' é Alfanumerico? ', n1.isalnum())
print(n1, ' é alfaberico? ', n1.isalpha())
print(n1, ' é Ascii? ', n1.isascii())
