from time import sleep
primeiro_termo = float(input('Digite o primeiro numero da PA: '))
razao = int(input('Digite a razão da PA: '))
ntermos = int(input('Digite o numero de termos da pa: ')) - 1
PA = [primeiro_termo]
while ntermos != 0:
    primeiro_termo = primeiro_termo + razao
    PA.append(primeiro_termo)
    ntermos = ntermos -1
    if ntermos ==0:
        print(PA)
        pergunta =  str(input('Você aumentar o numero de termos da sua PA? S/N ')).strip().upper()
        if pergunta == 'S':
            ntermos = int(input('Em quantos numeros você pretende aumentar a sua PA? '))
print('Programa encerrado')
sleep(5)