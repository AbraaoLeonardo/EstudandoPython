peso_maior = 0
peso_menor = 0
for i in range(5):
    peso = float(input('Digite o peso: '))
    if peso_maior < peso or peso_maior == 0:
        peso_maior = peso
    if peso_menor > peso or peso_menor == 0:
        peso_menor = peso
print('O maior peso é {} kilo e o menor peso é {} kilo'.format(peso_maior, peso_menor))