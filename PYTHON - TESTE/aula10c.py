n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
m = (n1+n2)/2
print('Sua média final foi: {}'.format(m))
if m >= 5:
    print('Parabéns, você foi aprovado!')
else:
    print('Você foi reprovado, ESTUDE MAIS!')