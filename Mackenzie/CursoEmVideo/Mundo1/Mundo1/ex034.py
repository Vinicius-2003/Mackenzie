sal = float(input('Qual o seu salário : '))
if ( sal > 1250.00):
    novosal = sal * 1.1
else:
    novosal = sal * 1.15
print('O novo salário será de {:.1f}'.format(novosal))