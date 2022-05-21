#bibliotecas
from tkinter.tix import Tree
import emoji
import random
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
    if usuario.capitalize() == 'Pedra':
        print(emoji.emojize(':oncoming_fist:'))
        if pc == 'Pedra':
            print(emoji.emojize('Pedra! :oncoming_fist:'))
            print('Deu empate!!')
        if pc == 'Papel':
            print(emoji.emojize('Papel! :hand_with_fingers_splayed:'))
            print('Ganhei!! Papel cobre preda!')
        if pc == 'Tesoura':
            print(emoji.emojize('Tesoura! :victory_hand:'))
            print('Mas o que.. Perdi! Pedra quebra Tesoura...!')


    elif usuario.capitalize() == 'Papel':
        print(emoji.emojize(':hand_with_fingers_splayed:'))
        if pc == 'Papel':
            print(emoji.emojize('Papel! :hand_with_fingers_splayed:'))
            print('Deu empate!!')
        if pc == 'Pedra':
            print(emoji.emojize('Pedra! :oncoming_fist:'))
            print('Perdi!!...Papel cobre preda!')
        if pc == 'Tesoura':
            print(emoji.emojize('Tesoura! :victory_hand:'))
            print(emoji.emoji.emojize('Ganhei!! Tesoura corta papel!'))
            

    elif usuario.capitalize() == 'Tesoura':
        print(emoji.emojize(':victory_hand:'))
        if pc == 'Tesoura':
            print(emoji.emojize('Tesoura! :victory_hand:'))
            print('Deu empate!!')
        if pc == 'Pedra':
            print(emoji.emojize('Pedra! :oncoming_fist:'))
            print('Ganhei!! Pedra quebra Tesoura!')
        if pc == 'Papel':
            print(emoji.emojize('Papel! :hand_with_fingers_splayed:'))
            print('Mas como?! Você ganhou...Tesoura corta papel...')
    else:
        usuario = input(emoji.emojize('Não entendi :thinking_face:'))