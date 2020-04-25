n = input('Qual seu nome inteiro? ').strip()
print('Seu nome tem Silva? ')
#print('{}'.format((n[(n.upper().find('SILVA')):(n.upper().find('SILVA'))+4]).upper() == 'SILVA')) #Está errado!
print('silva' in n.lower())
