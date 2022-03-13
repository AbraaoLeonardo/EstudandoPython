while True:
    numero = int(input('Digite o numero que você deseja ver a tabuada: '))
    print('=-' * 30)
    if numero >= 0:
        for i in range(10):
            print('{} X {} = {}'.format(numero, i + 1, numero * (i+1)))
    else:
        break
    print('=-' * 30)
print('programa encerrado')