velocidade = int(input('Qual é a velocidade que o seu carro está se movendo? '))
if velocidade <= 80:
    print('Tenha um bom dia!')
else:
    print('Voce foi multado, e o valor da multa é de R${} '.format((velocidade-80)*7))