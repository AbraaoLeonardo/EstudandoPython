lista = []
lista_menor_peso = []
maior_peso = 0
menor_peso = 99999999
lista_maior_peso = []
while True:
    nome = str(input('Digite um nome: ')).strip().capitalize()
    peso = int(input('Digite um numero: '))
    lista.append([nome, peso])
    condicao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if peso < menor_peso:
        menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    while True:
        if condicao not in 'SN':
            condicao = str(input('Opção não encontrada. [S/N]')).strip().upper()
        else:
            break
    if condicao == 'N':
        break
for i in lista:
    if i[1] == menor_peso:
        lista_menor_peso.append(i[0])
    if i[1] == maior_peso:
        lista_maior_peso.append(i[0])

print(f'ao todo você matriculou {len(lista)}pessoas, sendo elas{lista}')
print(f'O menor peso é {menor_peso}')
print(f'O maior peso é {maior_peso}')
print(f'Esses são os alunos com menor peso {lista_menor_peso}')
print(f'Esses são os alunos com maior peso {lista_maior_peso}')
