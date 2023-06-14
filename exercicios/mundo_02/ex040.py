'''

 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

'''



""" print('\t Central de Notas')
print('-------------------------------------')
nome_aluno = input('Nome do aluno: ')

print('-------------------------------------')
print(f'Bem-vindo(a) a Central, {nome_aluno}')
print(f'Aluno: {nome_aluno}')
print('-------------------------------------') """

nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))

média = (nota_1 + nota_2) / 2

if média >= 7.0:
    print(f'Aluno aprovado com média {média:.1f}. Meus parabéns!')
elif 5.0 <= média <= 6.9:
    print(f'Aluno em recuperação com média {média:.1f}!')
else:
    print(f'Aluno reprovado com média {média:.1f}!')