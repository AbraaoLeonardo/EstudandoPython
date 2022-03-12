from random import randint
from time import sleep
escolha_do_computador = randint(0, 2)
print('Pedra = 0, Papel = 1 e Tessoura = 2')
escolha_do_player = int(input('Escolha a sua jogada: '))
Jogada = ['Pedra', 'Papel', 'Tessoura']
if escolha_do_player <= 2 and escolha_do_player >= 0:
    print('=' * 30)
    sleep(3)
    if escolha_do_player == escolha_do_computador:
        print('Empate, ambos escolheram {}'.format(Jogada[escolha_do_player]))
    elif escolha_do_player > escolha_do_computador:
        if escolha_do_player == 2 | escolha_do_computador == 0:
            print('Perdi, eu joguei {} e o computador jogou {}'.format(Jogada[escolha_do_player],
                                                                       Jogada[escolha_do_computador]))
        else:
            print('Ganhei, eu joguei {} e o computador jogou {}'.format(Jogada[escolha_do_player],
                                                                        Jogada[escolha_do_computador]))
    else:
        print('perdi')
else:
    print('Jogada não encontrada')