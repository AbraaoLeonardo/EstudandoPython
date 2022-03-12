salario = float(input('Digite o salario do funcionário: '))
if salario <= 1250.00:
    salario = salario * 1.15
else:
    salario = salario * 1.10
print('O salario do funcionário após os ajuste será de {:.2f}'.format(salario))