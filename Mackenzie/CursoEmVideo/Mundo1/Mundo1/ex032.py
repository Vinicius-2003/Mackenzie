from datetime import date
ano = int(input('Aperte 0 para saber do ano atual. Ou escreva o Ano : '))
if (ano == 0):
    ano = date.today().year
if (ano % 4 == 0)and (ano % 100 != 0) or  (ano % 400 == 0):
    print('\033[1;32mEste ano é bissexto!!!\033[m')
else:
    print('\033[31mEste ano não é bissexto :(\033[m')
    