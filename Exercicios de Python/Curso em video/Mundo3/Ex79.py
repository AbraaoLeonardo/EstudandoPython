lista = []
while True:
    num = int(input('Digite um numero: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Numero ja existe na lista')
    ask = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while True:
        if ask not in 'SN':
            ask = str(input('Operação invalida: [S/N]')).strip().upper()
        else:
            break
    if ask == 'N':
        break
print('=-'*30)
print(f'Você digitou os valores {lista}')
