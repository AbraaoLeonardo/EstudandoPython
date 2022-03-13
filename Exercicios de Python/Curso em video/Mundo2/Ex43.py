peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/(altura*altura)
print(imc)
if imc < 18.5:
    print('Abaixo da média')
elif 18.5 <= imc <=25:
    print('Dentro do peso')
elif 25 < imc <=30:
    print('Sobrepeso')
elif 30 < imc <=40:
    print('Obesidade')
else:
    print('Obesidade morbida')
