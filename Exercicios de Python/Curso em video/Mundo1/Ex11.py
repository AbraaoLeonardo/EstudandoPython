altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('A area da sua parede é {:.2f}m² e precisará de {:.2f}l de tinta'.format(area, area/2))