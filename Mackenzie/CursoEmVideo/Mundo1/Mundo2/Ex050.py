s = 0
for a in range(1,7):
    num = int(input('Digite um valor : '))
    if ( num % 2 == 0 ):
        s += num
print('\033[1;34mA soma dos valores pares digitados foi\033[m\033[1;31m{}\033[m'.format(s))