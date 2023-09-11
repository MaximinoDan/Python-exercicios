# 3° Desafio - Crie um script Python que leia dois números e tente mostrar a soma entre eles.

n1 = int(input ('Digite um número:')) 
n2 = int(input ('Digite mais um número:'))
s = n1 + n2
# 1° maneira de print
#      print('A soma vale', s)
# 2° maneira de print
print('A soma vale {}'.format(s))