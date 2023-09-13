'''Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
   Faça um programa que leia o nome dos quatro alunos e mostre a ordm sorteada.'''

'''1ª Maneria de executar com importação'''
'''
import random

n1 = str(input("Primeiro Nome: "))
n2 = str(input("Segundo Nome: "))
n3 = str(input("Terceiro Nome: "))
n4 = str(input("Quarto Nome: "))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de apresentação será")
print(lista)
'''

'''2ª Maneira de executar importando direto na função'''

from random import shuffle

n1 = str(input("Primeiro Nome: "))
n2 = str(input("Segundo Nome: "))
n3 = str(input("Terceiro Nome: "))
n4 = str(input("Quarto Nome: "))

lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação será")
print(lista)
