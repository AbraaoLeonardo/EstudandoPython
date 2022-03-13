from time import sleep
maior = 0
menor = 9999999999999999999
soma = 0
quantidade = 0
while True:
    numero = int(input('Digite um numero: '))
    soma += numero
    quantidade += 1
    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero
    continuar = str(input('Deseja continuar? S/N ')).strip().upper()
    while continuar not in 'NS':
        continuar = str(input('comando invalido, digite S - para continuar ou N - para parar: ')).strip().upper()
        if continuar == 'N':
            break
    if continuar == 'N':
        break
print('A quantidade de numeros digitado foi {}, sendo o menor {} o maior é {} a soma é {} e a média é {}'.format(quantidade, menor, maior, soma, soma/quantidade))
sleep(10)