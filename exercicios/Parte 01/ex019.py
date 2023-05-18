# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice
from time import sleep
import emoji

a = input('Primeiro aluno(a): ')
b = input('Segundo aluno(a): ')
c = input('Terceiro aluno(a): ')
d = input('Quarto aluno(a): ')

sorteio = a, b, c, d
escolha = choice(sorteio)

sleep(0.5)

print(emoji.emojize('O aluno escolhido foi... :question:', language='alias'))

sleep(0.20)

print(emoji.emojize(f'{escolha}! Meus parabéns! :tada:', language='alias'))




