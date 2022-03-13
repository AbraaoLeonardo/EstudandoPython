tupla = ('curso', 'basico', 'de', 'python', 'do', 'curso', 'em', 'video')
print('*' * 50)
for i in tupla:
    print(f'\na palavra {i} possui essas vogais: ', end='')
    for j in i:
        if j in 'aeiou':
            print(j, end=' ')
print('\n', '*' * 50)
