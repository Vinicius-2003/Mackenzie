a = int(input('\033[1;34mMe fale um valor para a : \033[m'))
b = int(input('\033[1;34mMe fale um valor para b : \033[m'))
c = int(input('\033[1;34mMe fale um valor para c : \033[m'))
if ( a < b + c) and ( b < a + c ) and ( c < a + b):
    print('É um triângulo!')
    if ( a == b == c):
        print('\033[1;33mTriangulo Equilátero!\033[m')
    elif (a == b) and (b != c ) and ( a != c):
        print('\033[1;35mTriangulo Isóceles!\033[m')
    else:
        print('\033[1;32mTriangulo Escaleno!\033[m')
else:
    print('\033[1;31mNão formará um triangulo! :(\033[m')       