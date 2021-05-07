from random import randint
computador = randint(0,5) #Faz o computador pensar
print('-=-' * 10)
print('Vou pensar em um número, tente adivinhar ...')
print('-=-' * 10)
jogador = int(input("Em que número pensei: "))
print('CARREGANDO ...')
if jogador == computador:
    print('Prabéns, você ganhou!')
else:
    print('GANHEI, eu pensei no número {} e não {}!'.format(computador, jogador))
