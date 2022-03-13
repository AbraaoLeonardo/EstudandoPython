lista = []
lista_par = []
lista_impar = []
while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    condicao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while True:
        if condicao not in 'SN':
            condicao = str(input('Opção não encontrada. [S/N]')).strip().upper()
        else:
            break
    if condicao == 'N':
        break
for i in range(len(lista)):
    if lista[i] % 2 == 0 or lista[i] == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])
print('*'*50)
print(f'a lista com todos os numeros é: {lista}')
print(f'a lista com numeros inpares é: {lista_impar}')
print(f'a lista com numeros pares é: {lista_par}')

