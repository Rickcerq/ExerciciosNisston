from random import randint

escolhas = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
jogador = int(input("Selecione entre: 0 - Pedra, 1 - Papel e 2 - Tesoura: "))

print('O jogador escolheu {}'.format(escolhas[jogador]))
print('O computador escolheu {}'.format(escolhas[computador]))

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Papel amassa pedra, Jogador vence')
    elif jogador == 2:
        print('Pedra destroi tesoura, Computador vence')
    
elif computador == 1:
    if jogador == 0:
        print('Papel amassa pedra, Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Tesoura corta papel, Jogador vence')

elif computador == 2:
    if jogador == 0:
        print('Pedra destroi tesoura, Jogador vence')
    elif jogador == 1:
        print('Tesoura corta papel, Computador vence')
    elif jogador == 2:
        print('Empate')