# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Considrei U$1.00 = R$5,20

dindin = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = dindin / 5.20
euro = dindin / 5.52
libra = dindin / 6.25
franco = dindin / 5.55

print(f'Com R${dindin:.2f} você pode comprar US${dolar:.2f}')
print(f'Com R${dindin:.2f} você pode comprar €{euro:.2f} \nCom R${dindin:.2f} você pode comprar £{libra:.2f}')
print(f'Com R${dindin:.2f} você pode comprar Fr{franco:.2f}')





