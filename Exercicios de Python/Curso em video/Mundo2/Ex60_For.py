numero = int(input('Digite um numero: '))
fator = numero - 1
for i in range(numero - 1):
    numero = numero * fator
    fator = fator - 1
print(numero)