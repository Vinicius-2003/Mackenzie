#Exercicio 1

n = int(input('Número de termos : '))
if (1<=n<=20):
    seq = 1 
    t = 3
    for c in range(1,n+1):
        print(seq)
        seq = seq + t
        t+= 2
else:
    print('Termo Inválido!\033[m')

#Exercicio 2

import math 
num = int(input('Número para fatorial : '))
resultado = math.factorial(num)
if 0< num <= 15:
    for c in range(num,0,-1): 
        if c == 1:
            print(c, '=',resultado)
        else:
            print(c, 'x',end=' ')

#Exercicio 3(duvida)

num = int(input('Número : '))
if 1 < num <= 20:
    print('*' * num)
    for i in range(num-2):
        print('*',i*' ','*')
    print('*' * num)


#Exercicio 4

altura = int(input('Altura do triângulo : '))
for i in range(1,altura+1):
    print('*'*i)


#Exercicio 5

import math
e = 1
N = int(input('Número : '))
if N > 0 :
    for i in range(1,N+1):
        e = e + 1/math.factorial(i)
    print(e)

#Exercicio 6 (terminar)
import math
x = int(input('Informe o valor de X : '))
a = 1
for c in range(25,0,-1):
    total = 

#Exercicio 7
i = 1
total = 0
for c in range(1,51,1):
    total = total + (i/c)
    i += 2
print('Total = {:.1f}'.format(total))

#Exercicio 8

reajuste65 = 0
mulher = 0
homem = 0
numEmpreg = int(input('Qual o número de empregados da sua empresa? : '))
for c in range(1,numEmpreg+1):
    nome = str(input('Nome : '))
    sexo = str(input('F ou M = ')).upper()
    if sexo =='F':
        mulher += 1
    if sexo =='M':
        homem += 1
        salario = float(input('Digite seu salário : '))
        if salario < 850.00: 
            print('Número Inválido!')
        elif salario >= 3000.00:
            novo_sal= salario + ((salario*4.5)/100)
            med = novo_sal
            print('Seu novo salário será de {:.1f}R$'.format(novo_sal))
        elif salario >= 2000.00:
            reajuste65 += 1
            novo_sal = salario + ((salario*6.5)/100)
            med = novo_sal
            print('Seu novo salário será de {:.1f}R$'.format(novo_sal))
        elif salario < 2000.00:
            novo_sal = salario + ((salario*8.5)/100)
            med = novo_sal
            print('Seu novo salário será de {:.1f}R$'.format(novo_sal))
    else:
        salario = float(input('Digite seu salário : '))
        if salario < 850.00: 
            print('Número Inválido!')
        elif salario >= 3000.00:
            novo_sal= salario + ((salario*4.5)/100)
            print('Seu novo salário será de {:.1f}R$'.format(novo_sal))
        elif  2000.00<= salario < 3000.00:
            reajuste65 += 1
            novo_sal = salario + ((salario*6.5)/100)
            print('Seu novo salário será de {:.1f}R$'.format(novo_sal))
        elif salario < 2000.00:
            novo_sal = salario + ((salario*8.5)/100)
            print('Seu novo salário será de {:.1f}R$'.format(novo_sal))
            
 
print('A quantidade de empregados que receberam o reajuste de 6,5 porcento foi de {} empregados!'.format(reajuste65))
medreajuste = med/homem
print('O salário médio reajustado entre homens foi de {:.1f}R$'.format(medreajuste))
tot_mulher = (mulher/numEmpreg)*100
print('A quantidade de empregadas mulheres é {:.0f} porcento'.format(tot_mulher))



#Exercicio 9 

print('''[1 = Simone Tebet]
[2 = Bolsonaro]
[3 = Lula]
[4 = Padre Kelmon]
[5 = Voto Nulo]
[6 = Voto em Branco]''')
SimoneTebet = 0
Bolsonaro = 0
Lula = 0 
PadreKelmon = 0
Nulo = 0 
Branco = 0
votos = 0 
while True:
    eleições= int(input('Qual o número do seu candidato : '))
    if eleições < 0 or eleições > 6:
        break 
    if eleições == 1:
        SimoneTebet += 1
        votos += 1
    elif eleições == 2:
        Bolsonaro += 1
        votos += 1
    elif eleições == 3:
        Lula += 1
        votos += 1
    elif eleições == 4:
        PadreKelmon += 1
        votos +=1
    elif eleições == 5:
        Nulo +=1
        votos +=1
    elif eleições == 6:
        Branco +=1
        votos +=1
print(f'Simone Tebet possui {SimoneTebet} votos!')
print(f'\033[32mBolsonaro\033[m possui {Bolsonaro} votos!')
print(f'\033[31mLula\033[m possui {Lula} votos!')
print(f'Padre Kelmon possui {PadreKelmon} votos!')
print(f'Nulos contam com {Nulo} votos!')
print(f'Brancos possuem {Branco} votos!')
totnull = (Nulo/votos)*100
totwhite = (Branco/votos)*100
print('A porcentagem de votos nulos foi de {:.1f} porcento!'.format(totnull))
print('A porcentagem de votos brancos foram de {:.1f} porcento!'.format(totwhite))

