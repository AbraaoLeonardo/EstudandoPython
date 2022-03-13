inpar = []
multiplicacao = []
for i in range(500):
    x = i+1
    if x % 2 != 0 and x % 3 == 0:
        inpar.append(x)
        multiplicacao.append(int(x/3))
print(inpar)
print(multiplicacao)