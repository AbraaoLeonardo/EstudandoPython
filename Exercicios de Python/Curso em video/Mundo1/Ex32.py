ano = int(input('Digite o ano de pesquisa: '))
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('O ano de {} foi bissexto'.format(ano))
else:
    print('O ano de {} não foi bissexto'.format(ano))