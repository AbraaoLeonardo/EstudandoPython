maior = -99999999999999999999999
menor = 99999999999999999999999
lista = []
for i in range(5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero
print(f'o menor numero digitado foi {menor} e ele é o {lista.index(menor) + 1} numero da lista')
print(f'o menor numero digitado foi {maior} e ele é o {lista.index(maior) + 1} numero da lista')