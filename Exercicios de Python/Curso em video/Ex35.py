Primeiro_segmento = float(input('Primeiro segmento: '))
Segundo_segmento = float(input('Segundo segmento: '))
Terceiro_segmento = float(input('Terceiro segmento: '))
if Primeiro_segmento + Segundo_segmento > Terceiro_segmento and Primeiro_segmento + Terceiro_segmento > Segundo_segmento and Segundo_segmento + Terceiro_segmento > Primeiro_segmento:
    print('Os valore podem formar um triangulo')
else:
    print('Não podem formar um triangulo')