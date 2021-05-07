dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
print('Você alugou o carro por {} dias e rodou {}km.'.format(dias, km))
print('Logo deverá pagar o valor de R${:.2f}'.format((dias * 60) + (km * 0.15)))

