'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá msotrar o tempo que falta ou que passou do prazo.
'''
from time import sleep
from datetime import date

ano_nascimento = int(input('Em que ano você nasceu? '))
idade = abs(ano_nascimento - date.today().year)

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {format(date.today().year)}.')

if idade < 18:
    print('Processando...')
    sleep(4)
    alistamento = 18 - idade
    print(f'Ainda faltam {alistamento} anos para o seu alistamento ')
elif idade == 18:
    print(f'Você deve se alistar!')
else:
    alistamento = idade - 18
    print(f'Você deveria ter se alistado há {alistamento} anos')