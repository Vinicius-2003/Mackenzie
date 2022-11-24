prim = int(input('Qual o primeiro termo da progressão? : '))
passo = int(input('Qual o intervalo entre valorles? : '))
for c in range (prim,(passo * 11 - passo),passo):
     print(c)
print('Esses foram os 10 primeiros valores de uma PA ! ')