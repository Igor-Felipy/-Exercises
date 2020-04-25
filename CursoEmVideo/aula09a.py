frase = 'curso em video python'

# Fatiamento de string
print(frase[9:21:2]) #o primeiro numero representa o inicio de onde será printado, o segundo representa o final e o ultimo Significa que vai pulando de 2 em 2
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise de string
print(len(frase)) #comprimento
print(frase.count('o')) #conta a quantidade de letras em uma string
print(frase.count('o',0,13)) #conta as letras em um fatiamento de string
print(frase.find('deo')) #Pesquisa na string, e retorna o indice inicial da palavra ou -1 que representa not found
print('curso' in frase) #diz se existe uma string dentro de outra

# Transformação de string
print(frase.replace('Python','Android')) #substitui uma parte de uma string por outra coisa
print(frase.upper()) #deixa toda a string em maiusculo
print(frase.lower()) #deixa toda a string em minusculo
print(frase.capitalize()) #Coloca o primeiro caractere em maiusculo e todos os outros em minusculo
print(frase.title()) #Deixa o primeiro caractere das palavras em minusculo
fraseB = '   Aprenda Python  '
print(fraseB.strip()) #remove todos os espaços inuteis das frases
print(fraseB.rstrip()) #remove os espaços do lado direito da string (do final da string)
print(fraseB.lstrip()) #remove os espaços no lado esquerdo da string (do inicio da string)

# Divisão
print(frase.split()) #gera uma lista a partir de uma cadeia de caracteres
fraseC = frase.split()
print('-'.join(fraseC)) #gera uma String unica a partir de uma lista


print("""Olá esse é um teste de menu
item 1 - asfwwefs
item 2 - asfesfsf
item 3 - sjfhskdj""")# print utilizado para menus