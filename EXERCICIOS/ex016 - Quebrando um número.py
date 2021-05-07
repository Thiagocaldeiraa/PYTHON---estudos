import math
num = float(input('Digite um número: '))
inteiro = math.floor(num)
print(" o número é descrito como {}, porém, sua versão inteira é {}".format(num, math.floor(inteiro)))

from math import floor
num = float(input(" digite um número: "))
print(" o número é descrito como {}, porém, sua versão inteira é {}".format(num, floor(num)))

from math import trunc
num = float(input(" digite um número: "))
print(" o número é descrito como {}, porém, sua versão inteira é {}".format(num, trunc(num)))

num = float(input(" digite um número: "))
print(" o número é descrito como {}, porém, sua versão inteira é {}".format(num, int(num)))

#Todas essas formas chegam ao mesmo resultado#

