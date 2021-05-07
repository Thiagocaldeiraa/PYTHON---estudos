#nome = str(input('Digite seu nome: ')).strip()
#print('silva'in nome + nome.strip() + nome.capitalize())

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome contem Silva? {}'.format('silva'in nome.lower()))