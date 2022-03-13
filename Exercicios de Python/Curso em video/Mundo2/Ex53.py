frase = str(input('Digite uma frase: '))
palavra = frase.split()
juntos = ''.join(palavra)
inverso = ''
for letra in range(len(juntos)-1,-1,-1):
    inverso += juntos[letra]
print(juntos, inverso)
if juntos == inverso:
    print('A palavra {} é um palindromo de {}'.format(juntos, inverso))
else:
    print('Não são palindromos')