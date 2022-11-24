from random import randint 
print('-=-' * 20)
print('\033[1;32mVamos Jogar Jokênpo?\033[m')
print('-=-' * 20)
print('''Suas opções são:
[0] = pedra
[1] = papel
[2] = tesoura''')
itens = ('pedra','papel','tesoura')
comp = randint(0 ,2)
#print('O computador escolheu {}'.format(itens[comp]))
esc =int(input('Escolha : '))
if (comp == 0):
    if (esc == 0):
        print('Empate!')
    elif (esc == 1):
        print('Você ganhou..')
    elif(esc == 2):
        print('EU GANHEI!')
elif (comp == 1):
    if (esc == 0):
        print('EU GANHEI!!')
    elif ( esc == 1):
        print('Empatou!')
    elif(esc == 2):
        print('Você ganhou..')
elif (comp == 2):
    if (esc == 0):
        print('Você ganhou..')
    elif ( esc == 1):
        print('EU GANHEI!!')
    elif(esc == 2):
        print('Empatou!')
