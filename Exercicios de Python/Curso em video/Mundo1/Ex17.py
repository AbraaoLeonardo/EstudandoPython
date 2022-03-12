from math import sqrt
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
hipotenuza = sqrt(pow(cateto_adjacente, 2) + pow(cateto_oposto, 2))
print('Considerando o cateto adjacente de {} e o cateto oposto {}, temos uma hipotenuza de {}'.format(cateto_adjacente,cateto_oposto,hipotenuza))