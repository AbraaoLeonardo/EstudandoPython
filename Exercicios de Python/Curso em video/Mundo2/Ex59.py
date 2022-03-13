numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
while True:
    print('='*30)
    print('Soma = 1\nSubtração = 2\nMultiplicação = 3\nDivisão = 4\nFinalizar = 5')
    print('='*30)
    operacao = int(input('Digite a operação que você deseja fazer: '))
    if operacao == 1:
        print('A soma do numero {:.1f} e do numero {:.1f} é {:.1f}'.format(numero1, numero2, numero2 + numero1))
    elif operacao == 2:
        print('A subtração do numero {:.1f} e do numero {:.1f} é {:.1f}'.format(numero1, numero2, numero1 - numero2))
    elif operacao == 3:
        print('A multiplicação do numero {:.1f} e do numero {:.1f} é {:.1f}'.format(numero1, numero2, numero2 * numero1))
    elif operacao == 4:
        print('A divisão do numero {:.1f} e do numero {:.1f} é {:.1f}'.format(numero1, numero2, numero1 / numero2))
    elif operacao == 5:
        break
    else:
        print('Operação invalida, digite novamente')
print('\nMuito obrigado por utilizar a nossa calculadora')