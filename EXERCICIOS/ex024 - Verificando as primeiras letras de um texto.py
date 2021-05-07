##cidade = str(input('Digite a cidade em que você nasceu: '))
##print('Santo'in cidade + cidade.strip() + cidade.capitalize())

cidade = str(input('Digite a cidade em que você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')