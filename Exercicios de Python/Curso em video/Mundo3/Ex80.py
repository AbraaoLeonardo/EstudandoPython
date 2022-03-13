lista = []
for i in range(5):
    numero = int(input('Digite um numero: '))
    if i == 0 or numero > lista[len(lista)-1]:
       lista.append(numero)
       print(f'O valor {numero} será adicionado na pocisão {i}')
    else:
        pos = 0
        while pos < len(lista):
            if lista[pos] >= numero:
                lista.insert(pos, numero)
                print(f'O valor {numero} será adicionado na pocisão {pos}')
                break
            pos += 1
print('X'*40)
print(lista)
print('X'*40)