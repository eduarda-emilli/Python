# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite

velocidade = float(input('Digite a velocidade do carro em (em km/h): '))

if velocidade > 80:
    print('Você foi multado!')
    km_acima = velocidade - 80
    multa = km_acima * 7
    print(f'A multa é de R$ {multa:.2f}')
else:
    print('Parabéns, você está dentro do limite de velocidade.')



