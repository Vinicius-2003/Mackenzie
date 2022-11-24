p = float(input('Seu peso : '))
a = float(input('Susa altura : '))
imc = (p / (a * a))
if imc < 18.5: 
    print('\033[1;30;41mAbaixo do peso! \033[m')
elif 18.5 <= imc < 25:
    print('\033[1;30;42mPeso Ideal\033[m')
elif 25 <= imc < 30:
    print('\033[1;30;41mSobrepeso!\033[m')
elif 30 <= imc < 40:
    print('\033[1;30;41mObesidade!\033[m')
elif imc > 40:
    print('\033[1;30;41mObesidade Mórbida!\033[m')