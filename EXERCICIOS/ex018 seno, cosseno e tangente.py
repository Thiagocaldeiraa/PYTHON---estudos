import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do seno é {:.2f}'.format(seno))
print('O valor do cosseno é {:.2f}'.format(cosseno))
print('O valor da tangente é {:.2f}'.format(tangente))
