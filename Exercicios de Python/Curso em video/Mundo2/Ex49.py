numero = float(input('Digite um numero: '))
for i in range(10):
    tabuada = numero * i
    print('{} X {} = {:.1f}'.format(numero, i, tabuada))