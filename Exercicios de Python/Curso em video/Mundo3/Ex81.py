lista = []
sim = 0
while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    if numero == 5:
       sim += 1
    condicao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while True:
        if condicao not in 'SN':
            condicao = str(input('Opção não encontrada. [S/N]')).strip().upper()
        else:
            break
    if condicao == 'N':
        break
print('*'*50)
print(lista)
if sim != 0:
    print('Sim, o numero 5 foi encontrado :)')
else:
    print('Numero 5 não encontrado: ')