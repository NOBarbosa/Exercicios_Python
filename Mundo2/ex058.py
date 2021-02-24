'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o
 jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
num_pc = randint(0, 10)
print('Vamos jogar?')
print('Vou pensar em um número entre 0 e 10')
print('Você consegue adivinhar qual número pensei? ')
acertou = False
cont = 0
while not acertou:
    num = int(input('Qual o seu palpite? '))
    cont += 1
    if num == num_pc:
        acertou = True
    else:
        if num < num_pc:
            print('mais.. tente outra vez: ')
        else:
            print('menos.. tente novamente')
print('Você acertou em {} tentativas. Parábens!'.format(cont))
