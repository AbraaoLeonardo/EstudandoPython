brasileirao = ('Atletico MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'Ameria-MG', 'Atético-go', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Atletico-PR', 'Cuiaba', 'Juventude', 'Gremio', 'Bahia', 'Sport', 'Chapecoense')
print('Os 5 primeiros colocados são:', brasileirao[:5])
print('\nOs times que serão rebaixados são:', brasileirao[16:20], '\n')
print(sorted(brasileirao))
print('\nO Chapecoense está na {} pocisão'.format(brasileirao.index('Chapecoense') + 1))