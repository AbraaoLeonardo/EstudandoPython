homems = 0
mulheres = 0
maior = 0
cadastrados = 0
while True:
    idade = int(input('Digite a idade do funcionario: '))
    sexo = str(input('Digite o sexo da pessoa: [M/F] ')).strip().lower()
    cadastrados += 1
    if sexo == 'm':
        homems += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    if idade <= 18:
        maior += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while True:
        if continuar not in 'NS':
            continuar = str(input('Valor invalido, digite S - para continuar e N para parar: ')).strip().upper()
        else:
            break
    if continuar == 'N':
        break
print('Foram cadastradas {} pessoas, sendo {} homens, {} mulheres menores de 20 anos e {} pessoas menores de 18'.format(cadastrados, homems, mulheres, maior))


