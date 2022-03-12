from math import sqrt
numero = float(input('Digite um numero: '))
print('O numero digitado é {}, o seu dobro é {}, o triplo é {} e a sua raiz é {}'.format(numero, numero*2, numero*3, sqrt(numero)))

#Outra forma de resolver é:
#print('O numero digitado é {}, o seu dobro é {}, o triplo é {} e a sua raiz é {}'.format(numero, numero*2, numero*3, pow(numero,0.5)))