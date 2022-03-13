lista = ('Melancia', 3.8, 'Maca', 1.9, 'Banana', 0.9, 'Uva', 4.30, 'Maracuja', 6.80)
print(50 *'_')
for i in range(0, len(lista)-1,2):
    print(lista[i], '-' * (40 - len(lista[i])), 'R$', lista[i+1])
print(50*'_')