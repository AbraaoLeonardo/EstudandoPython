termo1 = float(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
PA = []
termox = 0
for i in range(10):
    termox = termo1 + (razao * (i))
    PA.append(round(termox, 1))
print(PA)