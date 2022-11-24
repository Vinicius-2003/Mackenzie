num =  int(input('\033[mNúmero : \033[m')) # importante colocar 0 \033[m para que quando usar o código mais de uma vez não pinte as letras do código. 
tot = 0
for c in range(1, num+1): # cria-se um repetição de 1 até o número escolhido
    if num % c == 0: # caso o resultado da divisão do número pelo "contador" for 0 
        print('\033[33m', end ='') # pinta os divisores de amarelo
        tot +=1 # O total de divisores recebe mais 1
    else: # caso contrário ele pinta os números não divisiveis de vermelho
        print('\033[31m', end='') # o end ='' serve para 'somar' as linhas e escrever tudo em uma.
    print('{} '.format(c), end='')
if tot >2:
    a = 'NÃO É PRIMO'
else:
    a = 'É PRIMO'
print('\n\033[mO número {} , {} pois possui {} divisores!'.format(num,a,tot))

