c = input('Em que cidade você nasceu? ').strip()
print('santo' in (c.lower().split()[0]))
print(c[:5].upper() == ('SANTO'))
