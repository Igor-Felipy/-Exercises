from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
x = radians(a)
s = sin(x)
c = cos(x)
t = tan(x)
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(s, c, t))
