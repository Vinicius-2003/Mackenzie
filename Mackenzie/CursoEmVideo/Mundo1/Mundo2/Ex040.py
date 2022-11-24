a = float(input('Nota 1 : '))
b = float(input('Nota 2 : '))
med = (a +b)/2
if (med < 5.00):
    print('\033[1;31mreprovado!\033[m')
elif (med > 5.0) and (med < 6.9):
    print('\033[1;34mRecuperação!!')
else:
    print('\033[1;32mAprovado!!\033[m')