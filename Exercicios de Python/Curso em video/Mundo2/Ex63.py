numero = int(input('Digite um numero inteiro: '))
sequencia = int(input('Digite o tamanho da sequencia: '))
resultado = [numero]
i = 0
while i != sequencia:
    if numero == 0:
         numero = 1
         resultado.append(numero)
    if i - 1 == -1:
        resultado.append(resultado[i])
        print('numero')
    if i == 1:
        resultado.append(resultado[i-1] + resultado[i - 2])
        resultado.append(numero)
    i = i + 1
print(resultado)