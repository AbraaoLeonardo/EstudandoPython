numero = int(input('Digite um numero: '))
print('-'*10)
for i in range(10):
    print('O valor de {} X {} é: {}'.format(numero, i+1, numero*(i+1)))
print('-'*10)