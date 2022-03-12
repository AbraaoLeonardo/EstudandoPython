from random import shuffle
nome = []
for i in range(4):
    nomes = str(input('Digite o nome do aluno: '))
    nome.append(nomes)
shuffle(nome)
print('A nova ordem será: ', nome)