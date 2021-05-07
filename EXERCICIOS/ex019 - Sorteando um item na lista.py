from random import choice
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno sorteado para sair mais cedo foi {}. Parabéns!!!'.format(escolhido))



