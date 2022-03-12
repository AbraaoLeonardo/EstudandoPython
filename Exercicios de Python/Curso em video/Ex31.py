distancia =float(input('Qual é a distancia da viagem em kilometros? '))
if distancia <= 200:
    valor_pago = distancia * 0.5
    print('A viagem possui {}km e sairá por {}'.format(distancia,valor_pago))
else:
    valor_pago = distancia * 0.45
    print('A viagem possui {}km e sairá por {}'.format(distancia,valor_pago))