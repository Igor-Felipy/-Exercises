f = input('Digte uma frase: ').strip()
print('A letra A aparece {} vezes'.format(f.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(f.lower().find('a')+1))
print('A última letra A apareceu na posição {} '.format(f.lower().rfind('a')+1))
