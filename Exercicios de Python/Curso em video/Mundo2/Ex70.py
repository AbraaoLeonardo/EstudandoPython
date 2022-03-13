total = 0
produto_caro = 0
produto_barato = 9999999999999999
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    total = total + preco
    if preco > 1000:
        produto_caro += 1
    if produto_barato < preco:
        barato = nome
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while True:
        if continuar not in 'SN':
            continuar = str(input('Opção invalida, S - continuar, N - Parar')).strip().upper()
        else:
            break
    if continuar == 'N':
        break
print('='*30, 'fim da compra', '='*30)
print('O total da compra foi de {}\ndentre todos os produtos {} custam mais de 1000 \ne o mais barato é o {}'.format(total, produto_caro, nome))