from time import sleep
from datetime import date

while True:
    
    sexo = int(input('''[ 1 ] Para feminino
[ 2 ] Para masculino
Escolha uma opção: '''))
    if sexo in [1, 2]:
        break
    print('Opção inválida. Por favor, escolha 1 para feminino ou 2 para masculino!')

ano_nascimento = int(input('Ano de nascimento: '))
idade = abs(ano_nascimento - date.today().year)


print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {date.today().year}')
print('Analisando dados...')
sleep(2)

if sexo == 1:
    if idade < 18:
        alistament = 18 - idade
        print(f'Você não tem idade para se alistar, mas não precisa se preocupar. \nO alistamento militar não é obrigatório para mulheres.')
    elif idade == 18:
        print('Você possui idade, mas não precisa se alistar, pois não é obrigatório para mulheres.')
    elif idade > 18:
        print(f'Você passou da hora de se alistar, mas não deve se preocupar. \nO alistamento militar não é obrigátorio para mulheres.')
if sexo == 2:
    if idade < 18:
        alistamento = idade - 18
        print(f'Você ainda não tem idade para se alistar. \nFaltam {alistamento} anos para o seu alistamento!')
    elif idade == 18:
        print(f'Você possui {idade} anos, já pode se alistar!')
    elif idade > 18:
        print(f'Você passou da hora. Deveria ter se alistado há {alistamento} anos')


