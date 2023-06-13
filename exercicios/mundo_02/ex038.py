'''

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais

'''

n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))

if n1 > n2: 
    print('O PRIMEIRO valor é MAIOR!')
elif n2 > n1:
    print('O SEGUNDO valor é MAIOR.')
else:
    print('Os dois valores são IGUAIS')
    

""" Maior que: >
Menor que: <
Igual a: ==
Diferente de: != """