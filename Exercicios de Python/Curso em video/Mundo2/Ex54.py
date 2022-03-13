from datetime import date
ano = date.today().year
maiores = []
menores = []
for i in range(7):
    nascimento = int(input('Digite a data de nascimento: '))
    if ano - nascimento < 18:
        menores.append(nascimento)
    else:
        maiores.append(nascimento)
print('A quantidades de pessoas menores de idade são {}'.format(len(menores)))
print('A quantidades de pessoas maiores de idade são {}'.format(len(maiores)))
