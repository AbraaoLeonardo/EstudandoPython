primeiro_termo = float(input('Digite o primeiro numero da PA: '))
razao = int(input('Digite a razão da PA: '))
ntermos = int(input('Digite o numero de termos da pa: ')) - 1
PA = [primeiro_termo]
while ntermos != 0:
    primeiro_termo = primeiro_termo + razao
    PA.append(primeiro_termo)
    ntermos = ntermos -1
print(PA)