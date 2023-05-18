# Desenvolva um programa que leia o comprimento de três retas e diga ao usuárop se elas podem ou não formar um triangulo.

\033[0:30:41m

print('-='*20)
print('Analisador de Triângulo')
print('-='*20)
r1 = float(input('Primeiro Segmento'))
r2 = float(input('Segundo Segmento'))
r3 = float(input('Terceiro Segmento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')