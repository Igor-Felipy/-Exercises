#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Uma distância em metros: '))
print('A média de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(m, (m/1000), (m/100), (m/10), (m*10), (m*100), (m*1000)))
