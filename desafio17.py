'''Faça um program que leia o comprimento do Cateto Oposto e do Cateto Adjacente de um triâgulo retângulo. Calcule e mostre o comprimento da Hipotenusa.'''


''' 1º Maneira de calculo tradicional sem importação

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa vai medir {:.2f}".format(hi))'''

'''2º Maneira de calculo com importação    

import math

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))'''

'''3º Maneira de calculo com importação e direta na função'''   

from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))
