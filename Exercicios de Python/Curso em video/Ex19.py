#Meu programa
from numpy import random
numero_de_alunos = int(input('quantos alunos farão parte da seleção: '))
nome = []
for i in range(numero_de_alunos):
    nomes = str(input('Digite o nome do aluno: '))
    nome.append(nomes)
valor_sorteado = random.randint(len(nome)-1)
print('O aluno escolhido para apagar a lousa foi:', nome[valor_sorteado])