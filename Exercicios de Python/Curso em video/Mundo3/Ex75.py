from time import sleep

tupla = (int(input('digite o numero 1: ')),
         int(input('digite o numero 2: ')),
         int(input('digite o numero 3: ')),
         int(input('digite o numero 4: ')),
         int(input('digite o numero 5: ')),)
par = 0
possui3 = 'Não'
pares = []
for i in range(len(tupla) - 1):
    if tupla[i] % 2 == 0:
        par += 1
        pares.append(tupla[i])
    if tupla[i] == 3:
        possui3 = 'Sim'
print('_'*90)
print('Nos numeros digitados, o numero 9 apareceu {} vezes e dos numeros digitados, {} é par, sendo eles'.format(tupla.count(9), par), pares)
if possui3 == 'Sim':
    print('o primeiro numero 3 parareceu na pocisão {}'.format(tupla.index(3)))
else:
    print('Não possui numero 3')
print('_' * 90)
sleep(2)