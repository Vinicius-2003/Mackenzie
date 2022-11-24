import math
#Coletar as informações iniciais fundamentais
Xo = int(input('Informe o valor de X : '))
Yo = int(input('Informe o valor de Y : '))
print('A coordenada do ponto de origem é : ({},{})'.format(Xo,Yo))
N = int(input('Quantos pares ordenados serão informados? : '))
menor = 0.0
maior = 0.0
j = 0
k = 0
for c in range(1,N+1):  
    X = int(input('Informe o valor de X : '))
    Y = int(input('Informe o valor de Y : '))
    dist = math.sqrt(math.pow((X-Xo),2) + math.pow((Y-Yo),2))
    if (X - Xo) > 0:
        if (Y-Yo) > 0:
            print('1º Quadrante')
            if dist > maior:
                maior = dist
                if c == 1:
                    menor = maior
                    k=c
                j = c
            elif (dist < maior):
                if (dist < menor):
                    menor = dist
                    k=c
        elif (Y - Yo) < 0:
            print('4º Quadrante')
            if dist > maior:
                maior = dist
                if c == 1:
                    menor = maior
                j = c
            elif dist < maior:
                if (dist < menor):
                    menor = dist
                    k = c
    else:
        if (Y-Yo)> 0:
            print('2º Quadrante')
            if dist > maior:
                maior = dist
                if c == 1:
                    menor = maior
                j = c
            elif dist < maior:
                if (dist < menor):
                    menor = dist
                    k = c
        elif (Y-Yo)<0:
            print('3º Quadrante')
            if dist > maior:
                maior = dist
                if c == 1:
                    menor = maior
                j = c
            elif dist < maior:
                if (dist < menor):
                    menor = dist
                    k = c
    print(maior)
    print(menor)
print('O ponto de maior distância é o {} dista {} da origem'.format(j ,maior))
print('O ponto de menor distância é o {} dista {} da origem'.format(k, menor))
