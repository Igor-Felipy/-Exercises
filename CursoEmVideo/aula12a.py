nome = str(input('Qual é seu nome? '))
if nome == 'Igor':
    print('Q nome bonito!')
elif nome == 'Felipy':
    print('seu nome é bem comum!')
elif nome in 'Ana Vitoria claudia':
    print('que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))