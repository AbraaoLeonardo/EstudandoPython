tupla = ('zero','um', 'dois', 'treis', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
valor_a_ser_procurado = int(input('Digite um numero de 0 a 20: '))
while True:
    if 0 <= valor_a_ser_procurado < 21:
        print('O numero digitado é: ', tupla[valor_a_ser_procurado])
        break
    else:
        print('Fora de escala')
        valor_a_ser_procurado = int(input('Digite um numero de 0 a 20: '))