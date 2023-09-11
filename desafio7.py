# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
soma = nota1 + nota2
media = soma / 2

print('A soma  da Primeira nota {} + {} da segunda nota é {} , e sua média de nota é: {}'.format(nota1, nota2, soma, media))