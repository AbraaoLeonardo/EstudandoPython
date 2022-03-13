from time import sleep
numero_a_fatorar = int(input('Digite o numero a fatorar: '))
fator = (numero_a_fatorar - 1)
while True:
    if fator != 1:
        numero_a_fatorar = numero_a_fatorar * fator
        fator = fator - 1
        print(fator)
        print(numero_a_fatorar)
        sleep(3)
    else:
        break
print(numero_a_fatorar)