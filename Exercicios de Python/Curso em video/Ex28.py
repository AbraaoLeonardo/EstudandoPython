import random as rd
from time import sleep
print('-='*30)
escolha_do_computador = rd.randint(0, 5)
escolha_do_jogador = int(input('Digite um numero de 0 a 5: '))
print('-='*30)
if escolha_do_jogador >= 0 | escolha_do_jogador <= 5:
    sleep(3)
    print('-=' * 30)
    if escolha_do_computador == escolha_do_jogador:
        print('Ganhei! Advinhei o numero do computador')
    else:
        print('Perdi, o numero escolhido foi', escolha_do_computador)
else:
    print('Numero fora do escopo')