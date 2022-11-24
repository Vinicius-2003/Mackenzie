# Numero de até 4 digitos

num = int(input('Número : '))
u = (num // 1) % 10
d = ( num // 10) % 10
c = (num // 100) % 10
m = (num // 1000)
print('unidade: ' , u)
print('dezena: ' , d)
print('centena: ' , c)
print('milhar: ' , m)
