matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(3):
        matriz[i][j] = int(input('Digite um numero: [{} {}]: '.format(i + 1, j + 1)))
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'[  {matriz[i][j]}  ]', end=' ')
        if j == len(matriz) - 1:
            print('\n')
