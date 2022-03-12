frase = str(input('Digite o seu nome: ')).strip().upper()
print('A frase possui {} letras A'.format(frase.count('A')))
print('A primeira letra A aparece na pocisão: ', frase.find('A')+1)
print('A ultima letra A aparece na pocisão: ', frase.rfind('A')+1)