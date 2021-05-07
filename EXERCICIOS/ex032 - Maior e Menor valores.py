num1 = int(input("Primeiro Valor: "))
num2 = int(input("Segundo Valor: "))
num3 = int(input("Terceiro Valor: "))
menor = num1
#Descobrindo o valor do menor número
if  num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print("O menor valor é {}".format(menor))
maior = num1
#Descobrindo o valor do maior número
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print("O maior valor é {}".format(maior))
