# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos. Faça um programa que leia o nome de
# quatro alunos e mostre a ordem sorteada.



from random import shuffle

a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')

lista = [a, b, c, d]

shuffle(lista)

print(f'A ordem de apresentação é {lista}')
