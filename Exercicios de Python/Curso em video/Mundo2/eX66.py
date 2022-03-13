soma = 0
quantidade = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma = soma + numero
    quantidade += 1
print('Foram adicionados {} numeros, e a soma desses numeros deu {}'.format(quantidade, soma))