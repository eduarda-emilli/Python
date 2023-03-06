# escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milímetros

print('\t----Conversão de medidas----')
medida = float(input('Informe o valor em metros: '))

cm = medida * 100
mm = medida * 1000
km = medida * 0.001
dm = medida * 10

print(f'A medida em cm de {medida}m é {cm}cm \nO mm de {medida}m é {mm}mm \nO quilômetro de {medida}m é {km}km')
print(f'O dm de {medida}m é {dm}')



