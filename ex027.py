n = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer! ')
print('Seu primeiro nome é: {}'.format(n.split()[0]))
print('Seu ultimo nome é: {}'.format(n.split()[n.count(" ")]))
