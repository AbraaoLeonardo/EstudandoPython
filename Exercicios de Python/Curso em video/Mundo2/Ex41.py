from datetime import date
ano = date.today().year
nascimento = int(input('Digite sua data de nascimento: '))
idade = ano - nascimento
if idade < 10:
    print('Atleta mirim')
elif 15 > idade >= 10:
    print('Atleta infantil')
elif 20 > idade >= 15:
    print('Atleta junior')
elif idade == 20:
    print('Atleta seniro')
else:
    print('Atleta master')