# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Qual a altura da parede:'))
largura = float(input('Qual a largura da parede:'))
metros = altura * largura
tinta = metros / 2

print('Você possui {}m² de parede e será necessário {} litros de Tintas para pintura'.format(metros, tinta))