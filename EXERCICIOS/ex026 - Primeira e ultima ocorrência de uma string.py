frase = str(input('Digite uma frase: ')).upper().strip()
print('a letra A aparece {} vezes'.format(frase.count('A')))
print('a letra A aparece pela primeira vez na casa {}'.format(frase.find('A')))
print('a letra A aparece pela ultima vez na casa {}'.format(frase.rfind('A')))
