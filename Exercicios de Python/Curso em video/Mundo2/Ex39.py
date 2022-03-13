from datetime import date
atual = date.today().year
nascimento = int(input('Digite a sua data de nascimento: '))
idade = atual - nascimento
if idade < 18:
    print('Ainda não se alistou, e faltam {} anos para se alistar: '.format(18-idade))
elif idade == 18:
    print('Precisa se alistar')
else:
    print('fazem {} anos que se alistou'.format(idade - 18))