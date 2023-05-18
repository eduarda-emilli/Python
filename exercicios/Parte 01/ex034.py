# Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a 1.250, calcule um aumento de 10%

# Para os inferiores ou iguais, o aumento é de 15%

sa = float(input('Qual o seu salário atual? R$ '))

au1 = sa + (sa * 15 / 100)
au2 = sa + (sa * 10 / 100)

if sa <= 1250:
    print(f'Você acaba de receber um aumento de 15%, seu sálario a partir de agora será de R$ {au1:.2f}')
else:
    print(f'Você acaba de receber um aumento de 10%, seu sálario a partir de agora será de R$ {au2:.2f}')




