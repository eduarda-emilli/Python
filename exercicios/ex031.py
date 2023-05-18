# Desenvolva um programa que pergfunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobranco 0,50 centavos por KM para viagens
# de até 200km a 0.45 centavos para viagens mais longas

distancia = float(input('Qual a distância da sua viagem? '))
print(f'A sua viagem será de {distancia}Km ')
if distancia <= 200:
    preço = distancia * 0.50
    print(f'O preço da sua passagem será de R${preço:.2f}')
else:
    preço = distancia * 0.45
    print(f'O preço da sua passagem será de R${preço:.2f}')