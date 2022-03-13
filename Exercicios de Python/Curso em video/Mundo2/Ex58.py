from random import randint
jogada_do_computador = randint(0, 10)
jogada_do_jogador = int(input('Digite um numero entre 0 a 10: '))
while jogada_do_jogador is not jogada_do_computador:
    jogada_do_computador = randint(0, 10)
    print('Eu escolhi {:.0f} e o computador escolheu {:.0f}'.format(jogada_do_jogador, jogada_do_computador))
    jogada_do_jogador = int(input('Perdi, escolha outro numero: '))
print('Ganhei, ambos escolhemos {:.0f}'.format(jogada_do_jogador))