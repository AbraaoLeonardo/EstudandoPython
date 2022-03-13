num = int(input('Digite um numero: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[32m', end='')
    print('{} '.format(i), end='')
if tot == 2:
    print('\n\nO numero é primo')
else:
    print('\n\nNão é primo pois é dividivel por {:.0f} valores'.format(tot))