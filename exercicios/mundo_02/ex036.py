'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Digite o valor da casa: R$ '))
salário = float(input('Digite o seu salário R$ '))
pagamento = int(input('Digite o prazo de pagamento  (em anos): '))

minimo = salário * 30 / 100

prestação = casa / (pagamento * 12)
print(f'Para pagar uma casa de R$ {casa:.2f} em {pagamento} anos', end='')
print(f' a prestação da casa será de R$ {prestação:.2f} reais')

if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')
