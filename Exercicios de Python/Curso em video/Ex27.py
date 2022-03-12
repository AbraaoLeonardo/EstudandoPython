nome = str(input('Digite o seu nome: ')).strip()
print('Muito prazer em te conhecer: ', nome)
print('O seu primeiro nome é', nome[:nome.find(' ')])
print('O seu Ultimo nome é', nome[nome.rfind(' ')+1:])
