lista = [[], []]
for i in range(0, 6):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        lista[1].append(numero)
    else:
        lista[0].append(numero)
print(f' A lista é {lista}')
lista[1].sort()
lista[0].sort()
print(f'Somente os pares são {lista[1]}')
print(f'Somente os impares são {lista[0]}')