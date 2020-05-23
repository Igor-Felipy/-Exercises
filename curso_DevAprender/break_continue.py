#Break
estilos_musicais = ['rock','pop','hip-hop','rap']

#rodar até que ele encontre o estilo musical "hip-hop"
for estilo in estilos_musicais:
    if estilo == 'hip-hop':
        break
    print(estilo)

for estilo in estilos_musicais:
    if estilo == 'pop':
        continue
    print(estilo)