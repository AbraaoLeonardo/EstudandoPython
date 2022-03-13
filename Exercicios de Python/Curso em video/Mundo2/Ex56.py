media = 0
idade_do_homem_mais_velho = 0
quantidades_de_mulheres_menores = 0
for i in range(4):
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo: M/F  ')).strip().upper()
    media = media + idade
    if sexo == 'M' and idade_do_homem_mais_velho < idade:
        homem_mais_velho = nome
        idade_do_homem_mais_velho = idade
    if sexo == 'F' and idade < 20:
        quantidades_de_mulheres_menores = quantidades_de_mulheres_menores + 1
print('a média das idades é {}'.format(media/4))
print('O homem mais velho é',homem_mais_velho)
print('O numero de mulheres menores de 20 é',quantidades_de_mulheres_menores)