# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas.

# O nome com todas as letras minúsculas.

# Quantas letras ao tem sem considerar os espaço.

# Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ').strip()

print('Analisando seu nome...')

nomemax = nome.upper()

print(f'Seu nome em maúsculas é {nomemax}')

nomemin = nome.lower()

print(f'Seu nome em minúsculas é {nomemin}')

print(f'Seu nome tem: {len(nome) - nome.count(" ")} letras')

find = nome.find(" ")

print(f'Seu primeiro nome tem {find} letras')

