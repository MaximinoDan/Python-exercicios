'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.]
ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6'''


'''RESOLUÇÃO 1 - MODULOS

import math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))'''

'''RESOLUÇÃO 2 - MODULOS ESPECIFICOS DA FUNÇÃO

from math import trunc
num = float(input('Digite um número : '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))'''

'''RESOLUÇÃO 3 - NÃO IMPORTAR

num = float(input('Digite um número: '))
print('O número {} tem a perte inteira {}'.format(num, int(num)))'''