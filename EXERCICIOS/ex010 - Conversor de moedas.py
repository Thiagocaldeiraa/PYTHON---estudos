real = float(input('Digite uma valor em reais: R$'))
print('R${} reais equivalem a US${:.2f} dólares.'.format(real, real/5.44))
print('R${} reais equivalem a €{:.2f} euros.'.format(real, real/6.56))
print('R${} reais equivalem a £{:.2f} libras.'.format(real, real/7.55))
print('R${} reais equivalem a ${} pesos argentinos.'.format(real, real*17.16))

