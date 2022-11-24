#Função seno x
import math as m 
x = 1
n = int(input('Até qual termo? : '))
soma = 0
i = 0
for i in range(0,n+1):
    soma = soma + m.pow((-1),i) * (m.pow(x,(2*i+1))/m.factorial(2*i+1))
print(soma)

