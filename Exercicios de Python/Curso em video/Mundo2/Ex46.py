from time import sleep
for i in range(11):
    explosao = 10 - i
    if explosao != 0:
        print(explosao)
    else:
        print('Booom!!!!!!!!!!!')
    sleep(1)