# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro pinta uma área de 2m²

print('\tPintando Parede')
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
litros = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m² \nPara pintar essa parede você precisará de {litros}l de tinta')

