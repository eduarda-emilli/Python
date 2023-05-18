# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
import time

num0 = randint(0,10)

print('          O computador está pensando em um número...          ')
time.sleep(3)
num = int(input('Digite o número que o computador pensou: '))

if num == num0:
    print(f'Você venceu!')
else:
    print(f'Você perdeu! O número pensado foi {num0}')





