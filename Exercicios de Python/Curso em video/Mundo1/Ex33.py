primeiro = int(input('Digite um numero: '))
segundo = int(input('Digite um numero: '))
terceiro = int(input('Digite um numero: '))
maior = primeiro
if primeiro < segundo and segundo > terceiro:
    maior = segundo
if segundo < terceiro and primeiro < terceiro:
    maior = terceiro
menor = primeiro
if primeiro > segundo and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and segundo > terceiro:
    menor = terceiro
print('O maior numero é {} e o menor é {}'.format(maior, menor))