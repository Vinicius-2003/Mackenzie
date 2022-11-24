vel = int(input('Qual a sua velocidade? (em km/h) : '))
if (vel > 80):
    multa = (vel - 80)*7
    print('\033[31mVocê foi multado :(\033[m')
    print('\033[31mO valor a ser pago será de {:.1f} R$\033[m'.format(multa))
else:
    print('\033[32mVocê estava dentro do limite :)\033[m')  