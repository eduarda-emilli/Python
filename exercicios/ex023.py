# Faça um programa que leia um npumero de 0 a 9999 e mostre na tela cada um dos seus digitos separados

# Ex: digite o número 1834

# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}')

print('--------------------------')

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

print('--------------------------')