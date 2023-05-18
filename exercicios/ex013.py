# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

nome = input('Digite o seu nome: ')
matricula = input('Digite a sua matrícula: ')

sa = float(input('Qual é o seu salário atual? R$ '))

au = sa + (sa * 15 / 100)

print(f'Parabéns {nome}! Você tem direito a um aumento de 15%, agora seu salário é de R$ {au:.2f}')
