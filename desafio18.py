'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, Cosseno e Tangente desse ângulo'''

'''1ª Maneira de executar com Importação Math'''
'''
import math

ângulo = float(input("Digite o ângulo desejado: "))
seno = math.sin(math.radians(ângulo))
print("O ângulo de {} tem o Seno de {:.2f}".format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print("O ângulo de {} tem o Cosseno de {:.2f}".format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print("O ângulo de {} tem a Tnagente de {:.2f}".format(ângulo, tangente))
'''

'''2ª Maneira de executar direto na função de Importação'''

from math import radians,sin,cos,tan

ângulo = float(input("Digite o ângulo desejado: "))
seno = sin(radians(ângulo))
print("O ângulo de {} tem o Seno de {:.2f}".format(ângulo, seno))
cosseno = cos(radians(ângulo))
print("O ângulo de {} tem o Cosseno de {:.2f}".format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print("O ângulo de {} tem a Tnagente de {:.2f}".format(ângulo, tangente))