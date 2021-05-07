km = float(input(" Informe a distância da viagem em km: "))
if km <= 200:
    valor = (km * 0.50)
    print("O valor da sua viagem será R${:.2f} !".format(valor))
else:
    valor2 = (km * 0.45)
    print("O valor da sua viagem será R${:.2f} !".format(valor2))

