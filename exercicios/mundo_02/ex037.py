''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal '''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
bi = bin(num)[2:]
oc = oct(num)[2:]
he = hex(num)[2:]
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bi}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oc}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é {he}')
else:
    print('[ERRO] Opção inválida')

    