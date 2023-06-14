""" 
# Faca um jogo de pedra papel e tesoura, onde o jogador e o computador escolhem entre 0-pedra 1-Papel 2-Tesoura.
# A jogada do computador é aleatória). 
# Jogo da pedra, tesoura e papel 
"""

from random import randint


escolha = int(
    input(
        """Escolha uma opção para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: """
    )
)

computador = randint(0, 2)

if computador == 0:
    print('Computador escolheu: Pedra')
    if escolha == 0:
         print("Empate!")
    elif escolha == 1:
        print("Ganhou")
    elif escolha == 2:
        print('Perdeu')
    
