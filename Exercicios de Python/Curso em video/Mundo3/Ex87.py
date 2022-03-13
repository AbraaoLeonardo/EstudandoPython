matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma3 = 0
maior = 0
for i in range(0, 3):
    for j in range(3):
        matriz[i][j] = int(input('Digite um numero: [{} {}]: '.format(i + 1, j + 1)))
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'[  {matriz[i][j]}  ]', end=' ')
        if j == len(matriz) - 1:
            print('\n')
        if matriz[i][j] % 2 == 0:
            soma_pares = soma_pares + matriz[i][j]
        if matriz[1][j] > maior or j == 0:
            maior = matriz[1][j]
for i in range(len(matriz)):
    soma3 = soma3 + matriz[i][2]
print(f'A soma dos pares é {soma_pares}')
print(f'A soma da terceira coluna é {soma3}')
print(f'O maior numero da coluna é {maior}')