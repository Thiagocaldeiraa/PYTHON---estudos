salario = float(input("Qual o salário do funcionário? R$ "))
aumento1 = (salario * 0.15) + salario
aumento2 = (salario * 0.10) + salario
if salario <= 1250:
    print("seu salário era de R${:.2f} e passou a ser R${:.2f}".format(salario, aumento1))
else:
    print(" Seu salário era de R${:.2f} e passou a ser R${:.2f}".format(salario, aumento2))