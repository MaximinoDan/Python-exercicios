# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000


print('{} metro(s), tem {} centimetros e {} milimetros'.format(medida, cm, mm))