valor = 0
for i in range(6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        valor = valor + num
if valor !=0:
    print('\nA soma dos numeros pares é', valor)
else:
    print('\nNenhum numero é par')