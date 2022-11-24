a = int(input('Me fale o valor do lado a : '))
b = int(input('Me fale o valor do lado b : '))
c = int(input('Me fale o valor do lado c : '))
if (a < b + c) and (b < a + c ) and (c < a + b):
    print('\033[1;32mIrá formar um triangulo!!!\033[m')
else:
    print('\033[31mNão forma um triangulo : (\033[m')