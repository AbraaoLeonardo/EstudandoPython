#expressao = str(input('Digite uma expressão: '))
##sem pilha
#abre = expressao.count('(')
#fecha = expressao.count(')')
#if abre == fecha:
#    print('Sua expressão está valida: ')
#else:
#    print('Sua expressão está errada: ')

##com pilha
expressao = str(input('Digite uma expressão: '))
pilha = []
for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) > 0:
    print('Sua expressão está errada: ')
else:
    print('Sua expressão está valida: ')