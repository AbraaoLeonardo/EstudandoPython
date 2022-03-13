from random import randint
from time import sleep

print('='*30)
print('vamos jogar par ou impar?')
print('='*30)
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 100)
    jogada = str(input('inpar ou par: [I/P] ')).strip().lower()
    sleep(2)
    print('Você jogou {} e a soma deu {}'.format(computador, computador+jogador))
    if jogada == 'p':
        resultado = (jogador + computador) % 2
        if resultado == 0:
            print('Ganhei!!!!!!!!. Vamos jogar novamente? ')
            print('Vamos')
        else:
            break
    if jogada == 'i':
        if resultado == 0:
            break
        else:
            print('Ganhei!!!!!!!!. Vamos jogar novamente? ')
            print('Vamos')
print('Perdi :( Não quero jogar mais')
sleep(3)
