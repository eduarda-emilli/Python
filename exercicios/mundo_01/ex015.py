# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar  sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado

dias =  int(input('Por quantos dias você alugou o carro? '))
km = int(input('Quantos Km você rodou? '))

pagar = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${pagar:.2f}')

