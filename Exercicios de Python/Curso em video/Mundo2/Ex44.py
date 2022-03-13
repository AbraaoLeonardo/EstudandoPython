valor = float(input('Digite o valor do produto: '))
print('='*30)
print('1 - a vista no dinheiro/cheque \n2 - à vista no cartão \n3 - em até 2 vezes no cartão \n4 - 3 vezes ou mais no cartão')
print('='*30)
forma_de_pagemento = int(input('Qual será a forma de pagamento? '))
if forma_de_pagemento == 1:
    valor_final = valor * 0.9
elif forma_de_pagemento == 2:
    valor_final = valor * 0.95
elif forma_de_pagemento == 3:
    valor_final = valor
elif forma_de_pagemento == 4:
    valor_final = valor * 1.20
else:
    print('Forma de pagamento invalida')
    valor_final = 0
if valor_final != 0:
    print('O valor final do produto será de {}'.format(valor_final))