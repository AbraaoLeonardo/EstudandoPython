nota1 = float(input('Digite a nota da P1: '))
nota2 = float(input('Digite a nota da P2: '))
media = (nota1+nota2)/2
if media < 5:
    print('A média do aluno foi {}, portanto está reprovado'.format(media))
elif media < 7 and 5 <= media:
    print('A média do aluno foi {}, portanto está de recuperação'.format(media))
else:
    print('A média do aluno foi {}, portanto está aprovado'.format(media))