'''

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.

'''

from math import trunc

real = float(input('Digite um valor: '))

result = trunc(real)

print(f'O valor digitado foi {real} e a sua porção inteira é {result}')

