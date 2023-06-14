""" 
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER 

"""
from datetime import date

ano_nascimento = int(input('Ano que o atleta nasceu: '))
idade_atleta = abs(ano_nascimento - date.today().year)
print(f'O atleta tem {idade_atleta} anos.')

if idade_atleta <= 9:
    print('Classificação: MIRIM')
elif idade_atleta  <= 14:
    print('Classificação INFANTIL')
elif idade_atleta  <= 19:
    print('Classificação JÚNIOR') 
elif idade_atleta  <= 25:
     print('Classificação SÊNIOR') 
else:
    print('Classificação MASTER')
    
    
    
    
