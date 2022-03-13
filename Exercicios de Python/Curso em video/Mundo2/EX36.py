casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite quantos anos você pretende parcelar a casa: '))
if casa/(anos*12) > salario*0.3:
    print('Imprestimo não altorizado')
else:
    print('Imprestimo aprovado, parcelas sairão no valor de {:.2f}'.format(casa/(anos*12)))
