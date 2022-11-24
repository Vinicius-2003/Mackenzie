for t in range(0,5):
    print('Oi')

#Contar até um número escolhido pelo usuário
n = int(input('Me fale um número de 0 a 10 : '))
for c in range(1, n+1):
    print(c)
print('Contei até o número que você escolheu! ')

#Contagem até o numero esolhido pelo usuário, no intervalo e com o fim também escolhido pelo mesmo.
i = int(input('Inicio : '))
f = int(input('Fim : '))
p = int(input('Passo : '))
for c in range ( i ,f+1,p):
    print(c)
print('Acabei de contar!!')


