# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO - MÉDIA 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota'))
m = (n1 + n2) / 2
if m < 5:
    print('Você tirou {:.1f}'.format(m))
    print('REPROVADO')
elif m >= 5 and m <= 6.9:
    print('Você tirou {:.1f}'.format(m))
    print('RECUPERAÇÃO')
else:
    print('Você tirou {:.1f}'.format(m))
    print('APROVADO')
