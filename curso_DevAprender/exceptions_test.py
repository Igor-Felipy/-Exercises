# Exceptions
try:
    ano_atual = int(input('Qual é o ano atual? '))
except ValueError:
    print('Você deve digitar um numero! ')

try:
    print(5/0)
except ZeroDivisionError:
    print('Não é possivel dividir por zero')

try:
    print(5/0)
except:
    print('Algo deu errado!')

try:
    print(5/0)
except:
    print('ocorreu um erro!')
finally:
    print('O resultado deu erro')


for pagina in range(10):
    try:
        print('buscando informação')
        print(5/0)
    except:
        pass
