numero = int(input('Digite o numero que você irá converter: '))
print('='*30)
print('1 - binário \n2 - octal \n3 - hexadecimal')
print('='*30)
opcoes = int(input('Escolha a base de conversão: '))
if opcoes == 1:
    print('{} convertido para binário é {}'.format(numero, bin(numero)))
elif opcoes == 2:
    print('{} convertido para octal é {}'.format(numero, oct(numero)))
elif opcoes == 3:
    print('{} convertido para hexadecimal é {}'.format(numero, hex(numero)))
else:
    print('Opção não encontrada')
