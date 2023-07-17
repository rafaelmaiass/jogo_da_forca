import random
import os

def boas_vindas():
    nome = input('Qual seu nome? ')
    print(f'Seja bem vindo {nome} ao Jogo da Forca.')
    print()
    print('Regras do jogo.\nVocê terá 6 chances de descobrir as letras de uma palavra misteriosa.')

def escolher_palavra():
    palavras = ['cruzeiro', 'navio', 'futebol', 'brasil', 'skate']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

boas_vindas()
palavra_secreta = escolher_palavra()
letras_corretas = []

print(f'A palavra tem {len(palavra_secreta)} letras.')
mostrar_palavra(palavra_secreta, letras_corretas)

inicio = input('Pressione s/n para iniciar o jogo...').lower()
os.system('cls')
contador_de_chances = 6

while inicio == 's':
    mostrar_palavra(palavra_secreta, letras_corretas)
    letra = input('Digite uma letra: ').lower()
    
    if contador_de_chances == 0:
        print('Você perdeu as 6 chances.')
        break
    
    if letra in palavra_secreta:
        letras_corretas.append(letra)
        if set(palavra_secreta) == set(letras_corretas):
            print('Você acertou a palavra, parabéns!')
            break
        
        else:
            print('Você acertou a letra, continue!')
    
    else:
        print('Você errou!\nTente novamente.')
        contador_de_chances -= 1
        print(f'Vidas restantes {contador_de_chances}')

    
