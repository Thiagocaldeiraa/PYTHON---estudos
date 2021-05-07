print('*=*' * 25)
print('VAMOS ANALISAR SE EXISTE UM TRIÂNGULO')
print('*=*' * 25)
r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))
#Fórmula para saber se existe um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Analisando as retas digitadas, EXISTE SIM um triângulo")
else:
    print("Analisando as retas digitadas, NÃO EXISTE um triângulo")