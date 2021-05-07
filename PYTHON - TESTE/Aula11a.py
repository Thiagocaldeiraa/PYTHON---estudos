#Trabalhando com cores no terminal PHYCHARM
#Sempre que quiser adicionar cores ao terminal, digita-se \33m[ style;text;bakc m
#Exemplo        \33[0;33;44m
#style =  0 sem estilo; 1 negrito; 4 underline; 7 inverte as cores;
#text = 30 branco; 31 vermelho; 32 verde; 33 amarelo; 34 azul; 35 roxo; 36 azul florescente e 37 cinza
#backgroound = 40 branco; 41 vermelho; 42 verde; 43 amarelo; 44 azul; 45 roxo; 46 azul florescente e 47 cinza
print("\33[0;36mTestando a paleta de cores")
print("\33[7;30;41mTestando a paleta de cores\33[m")

nome = str(input(" Digite seu nome: "))
print('É um prazer te conhecer \33[31m{}'.format(nome))