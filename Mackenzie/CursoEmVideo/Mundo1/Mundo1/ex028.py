#Método que eu fiz sozinho 
#Funciona

import random 
print('-=-' * 20)
escolhido = int(input('Escola um número de 0 a 5 : '))
print('-=-' * 20)
num = [1,2,3,4,5]
pensei = random.choice(num)
if (pensei == escolhido):
   print('eu pensei nesse número!!!VOCÊ GANHOU')
else:
    print('Não foi esse o número que eu escolhi, eu pensei no {}'.format(pensei))

#Resolução do Curso em Video

from random import randint
from time import sleep
print('-=-' * 20)
print('Estou pensando em um número, tente adivinhar...')
print('-=-' * 20)
comp = randint(0 ,5) #Numero que o computador vai escolher 
jog = int(input('Escolha um valor de 0 a 5 : '))
print('PROCESSANDO...')
sleep(2)
if (jog == comp):
    print('Você ganhou!!')
else:
    print('Você perdeu!!! Eu pensei no número {} e você no {}'.format(comp,jog))