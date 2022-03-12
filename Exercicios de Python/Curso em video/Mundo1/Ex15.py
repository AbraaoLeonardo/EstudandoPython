diarias = int(input('Quantos dias você ficou com o carro? '))
km_andados = int(input('Quantos kilometros você percorreu com o carro? '))
valor_a_pagar = (diarias * 60) + (km_andados * 0.15)
print('O valor a pagar é R${:.2f}'.format(valor_a_pagar))