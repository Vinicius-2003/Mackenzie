a = int(input('Número 1 : '))
b = int(input('Número 2 : '))
c = int(input('Número 3 : '))
menor = a
maior = a
if ( b < a ) and ( b < c ):
    menor = b 
if ( c < a ) and ( c < b ):
    menor = c
if ( b > a ) and ( b > c ):
        maior = b
if ( c > a ) and ( c > b ):
        maior = c
print('O maior valor será o {}'.format(maior))
print('O menor valor será o {}'.format(menor))