from math import sin, cos, tan, radians
angulo = int(input('digite um angulo: '))
print('Para o angulo {:.2f} \no seno é {:.2f} \no cos é {:.2f} \ne a tangente é {:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))