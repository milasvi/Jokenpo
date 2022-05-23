#bibliotecas
import emoji
import random
import pygame
pygame.init()

#sons
perdi = pygame.mixer.Sound('gameover.mp3.wav')
ganhei = pygame.mixer.Sound('coin.mp3.wav')
encerrei = pygame.mixer.Sound('winningmusic.wav')       


#cabecçalho
print('-='*25)
print(emoji.emojize('Jogue Pedra, Papel e Tesoura com o pc! :rock:  :roll_of_paper: :scissors:'))
print('-='*25)


#variaveis
lista = ['Pedra', 'Papel', 'Tesoura']
pc = ''
usuario = ''

#contadores
contadorG = 0
contadorP= 0
contadorE = 0



while True:
    pc = random.choice(lista)
    usuario = input('Pedra, Papel ou tesoura?')

    while usuario.capitalize() != 'Pedra' and usuario.capitalize() != 'Papel' and usuario.capitalize() != 'Tesoura':
        usuario = input(emoji.emojize('Não entendi :thinking_face:'))
    
    if usuario.capitalize() == 'Pedra':
        print(emoji.emojize(':oncoming_fist:'))
        if pc == 'Pedra':
            print(emoji.emojize('Pedra! :oncoming_fist:'))
            print('Deu empate!!')
            contadorE = contadorE + 1
        elif pc == 'Papel':
            print(emoji.emojize('Papel! :hand_with_fingers_splayed:'))
            print('\033[0;32mGanhei!!\033[m Papel cobre preda!')
            contadorP = contadorP + 1
            perdi.play
        else:
            print(emoji.emojize('Tesoura! :victory_hand:'))
            print('Mas o que.. Perdi! Pedra quebra Tesoura...!')
            contadorG = contadorG + 1
            ganhei.play


    elif usuario.capitalize() == 'Papel':
        print(emoji.emojize(':hand_with_fingers_splayed:'))
        if pc == 'Papel':
            print(emoji.emojize('Papel! :hand_with_fingers_splayed:'))
            print('Deu empate!!')
            contadorE = contadorE + 1
        elif pc == 'Pedra':
            print(emoji.emojize('Pedra! :oncoming_fist:'))
            print('Perdi!!...Papel cobre preda!')
            contadorG = contadorG + 1
            ganhei.play
        else:
            print(emoji.emojize('Tesoura! :victory_hand:'))
            print(emoji.emoji.emojize('\033[0;32m Ganhei!!\033[m Tesoura corta papel!'))
            contadorP = contadorP+ 1
            perdi.play

    elif usuario.capitalize() == 'Tesoura':
        print(emoji.emojize(':victory_hand:'))
        if pc == 'Tesoura':
            print(emoji.emojize('Tesoura! :victory_hand:'))
            print('Deu empate!!')
            contadorE = contadorE + 1
        elif pc == 'Pedra':
            print(emoji.emojize('Pedra! :oncoming_fist:'))
            print('\033[0;32m Ganhei!!\033[m Pedra quebra Tesoura!')
            contadorP = contadorP + 1
            perdi.play
        else:
            print(emoji.emojize('Papel! :hand_with_fingers_splayed:'))
            print('Mas como?! Você ganhou...Tesoura corta papel...')
            contadorG = contadorG + 1
            ganhei.play

    #repetição
    repeticao = input('Quer jogar mais uma vez?')
    while repeticao[0].capitalize() != 'N' and repeticao[0].capitalize() != 'S':
        repeticao = input('Não entendi, digite "sim" ou "não"')
    if repeticao[0].capitalize() == 'N':
        encerrei.play
        print(f'Ah que pena! \nVocê ganhou {contadorG} vezes, perdeu {contadorP} e empatamos {contadorE} vezes! \nObrigade por jogar comigo.\nAté mais!')
        break    
    