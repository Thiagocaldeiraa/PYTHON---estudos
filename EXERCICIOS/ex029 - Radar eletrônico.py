vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você foi multado, excedeu a velocidade de 80km/h!')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia. Dirija com cuidado!')



