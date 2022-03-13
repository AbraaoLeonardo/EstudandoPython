from random import randint
tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior = 0
menor = 9999999999999999999
for i in range(len(tupla) - 1):
    if maior < tupla[i]:
        maior = tupla[i]
    if menor > tupla[i]:
        menor = tupla[i]
print(tupla)
print(maior)
print(menor)