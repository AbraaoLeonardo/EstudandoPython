quantidade = 0
soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    else:
        soma += numero
        quantidade += 1
print('Foram digitados {} numeros, e a soma deles é {}'.format(quantidade, soma))