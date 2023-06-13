# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é par ou impar.

num = int(input('Digite um número qualquer: '))

res = num % 2

if res == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é ÍMPAR')



