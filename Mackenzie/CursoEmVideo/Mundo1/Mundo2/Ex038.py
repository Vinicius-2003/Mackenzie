a = int(input('\033[1;36mNúmero 1 : \033[m'))
b = int(input('\033[1;36mNúmero 2 : \033[m'))
if ( a > b ):
    print('O \033[1;33mprimeiro\033[m valor é o maior!')
elif ( b > a ):
    print('O \033[1;31msegundo\033[m valor é o maior!')
elif ( a == b ):
    print('\033[1;37mNão há valor maior, ambos são iguais!\033[m')
