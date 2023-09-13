'''Um professor quer sortear um dos seus alunos para apagar o quadro.
   Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido '''

'''1ª Maneira de executar com Importação'''
'''
import random

n1 = str(input("Primeiro Nome: "))
n2 = str(input("Segundo Nome: "))
n3 = str(input("Terceiro Nome: "))
n4 = str(input("Quarto Nome: "))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print("O aluno escolhido(a) foi {}".format(escolhido))
'''

'''2ª Maneira de executar importando direto na função'''

from random import choice

n1 = str(input("Primeiro Nome: "))
n2 = str(input("Segundo Nome: "))
n3 = str(input("Terceiro Nome: "))
n4 = str(input("Quarto Nome: "))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O aluno escolhido(a) foi {}".format(escolhido))