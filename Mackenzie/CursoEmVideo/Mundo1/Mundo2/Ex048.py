from time import sleep 
s = 0
for num in range (1,501):
   if (num % 3 == 0):
    s += num
sleep(1.0)
print('A soma de todos os números impares de 1 a 500 é \033[1;34m{}\033[m'.format(s))