salario = float(input('Informe seu salário: R$'))
aumento = salario + (salario * 0.15)
print('Seu salário atual é R${} e com o reajuste de 15% passará a receber R${:.2f}.'.format(salario, aumento))
