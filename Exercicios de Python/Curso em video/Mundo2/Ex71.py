from time import sleep

print('""'*30)
print('Bem vindo ao banco X')
print('""'*30)
valor = int(input('Digite quanto você deseja sacar: '))
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0
while True:
    if valor >= 50:
        valor = valor - 50
        c50 += 1
    elif valor >= 20:
        valor = valor - 20
        c20 += 1
    elif valor >= 10:
        valor = valor - 50
        c10 += 1
    elif valor >= 5:
        valor = valor - 5
        c5 += 1
    elif valor >= 2:
        valor = valor - 2
        c2 += 1
    elif valor == 1:
        valor = 0
        c1 = 1
    else:
        break
print('\n', '=-'*50)
print('A quantidade de notas será: ')
print('Cedulas de 50', c50)
print('Cedulas de 20', c20)
print('Cedulas de 10', c10)
print('Cedulas de 5', c5)
print('Cedulas de 2', c2)
print('Cedulas de 1', c1)
print('=-'*50)
sleep(5)