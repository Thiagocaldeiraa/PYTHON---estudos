#Estudando regras de 'FATIAMENTO' nas cadeias de texto

frase = "Thiago Caldeira da Silva"
print(frase[1]) #busca a letra correspondente a 1, lembrando que a string começa pelo 0.
print(frase[0:5]) #bucam as letras de 0 a 5
print(frase[0:15:2]) #buscam letras de 0 a 15 pulando de 2 e 2 casas.
print(frase[:7]) #buscam as letras do inicio até a casa 7.
print(frase[5:]) #buscam as letras da casa 5 até o final.
print(frase[9::3])#buscará da letra 9 ao final, porém, pulando 3 casas.

#Estudando regras de 'ANÁLISE' nas cadeias de texto
frase = "Thiago Caldeira da Silva"
print(len(frase)) #conta quantos caracteres possuem na frase.
print(frase.count('o')) #conta quantas letras 'o' possuem na frase.
print(frase.count('o',0,13)) #conta quantas letras 'o' da letra 0 a 13.
print(frase.find('eira')) #informa onde começou a frase 'eira'.
print(frase.find('jose')) #retornará -1 pois não existe na frase a palavra jose.
print('Silva'in frase) #buscará na frasé a palavra 'Silva', retornando verdadeiro pois existe na frase.

#Estudando regras de 'TRANSFORMAÇÃO' nas cadeias de texto
frase = "Thiago Caldeira da Silva"
print(frase.replace('Thiago', 'Lucas')) #Troca de palavras na frase.
print(frase.upper()) #transforma todas as letras em maiusculo.
print(frase.lower()) #transforma todas as letras em minusculo.
print(frase.capitalize()) #transforma a primeira letra em maisucula.
print(frase.title()) #transforma a primeira letra em maiscula onde possui espaço vazio.
print(frase.strip()) #remove todos os espaços antes e depois da frase
print(frase.rstrip()) #remove todos os espaços inuteis do lado direito.
print(frase.lstrip()) #remove todos os espaços inuteis do lado esquerdo.

#Estudando regras de 'DIVISÃO' nas cadeias de texto
frase = "Thiago Caldeira da Silva"
print(frase.split()) #Cada palavra da frase ficará em cadeias de caracteres.

#Estudando regras de 'JUNÇÃO' nas cadeias de texto
frase = "Thiago Caldeira da Silva"
print('-'.join(frase)) #Juntará e colocara - em toda frase
print(' '.join(frase)) #Juntará e colocara espaço em toda frase