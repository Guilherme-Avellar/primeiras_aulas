# jogo do pedra, papel ou tesoura, com biblioteca de sorteio


print("Jogo do pedra papel ou tesoura")
player = input("Joque pedra, papel ou tesoura: ")
from random import *
computador = randint(0,2)

if player == "pedra" or player == "Pedra" or player == "PEDRA":
    player = 0
else:
    if player == "papel" or player == "Papel" or player == "PAPEL":
        player = 1
    else:
        if player == "tesoura" or player == "Tesoura" or player == "TESOURA":
            player = 2
        else:
            computador = "O computador não jogou"
            player = 3

if player < 0 or player > 2:
    print("O jogo feito está escrito errado ou está inválido")
else:
    if player == computador:
        print("Empate")
    else:
        if (player == 0 and computador == 2) or (player == 1 and computador == 0) or (player == 2 and computador == 1):
            print("Você venceu")
        else:
            print("Derrota")

if computador == 0:
    computador = "O computador jogou pedra"
else:
    if computador == 1:
        computador = "O computador jogou papel"
    else:
        if computador == 2:
            computador = "O computador jogou tesoura"

print(computador)