from random import randint
from time import sleep

lista = []
todos_os_jogos = []
jogadas = int(input('Quantos jogos você quer jogar na mega sena? '))
jogos = 1
print('=='*60)
print(' '*60, f'numero de jogos {jogadas}', ' '*60)
print('=='*60)
while jogos <= jogadas:
    num = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            num += 1
        if num >= 6:
            break
    jogos += 1
    lista.sort()
    todos_os_jogos.append(lista[:])
    lista.clear()
for i in range(jogadas):
    print(f'jogo {i + 1} = {todos_os_jogos[i]} ')
    sleep(2)
print('='*56, 'Boa Sorte', '='*56)
sleep(10)
