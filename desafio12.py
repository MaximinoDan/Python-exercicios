# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$ '))
precoReal = preco - (preco * 5 / 100)

print('O produto que custava {}, na promoção com o  desconto de 5% vais custar {:.2f}'.format(preco, precoReal))