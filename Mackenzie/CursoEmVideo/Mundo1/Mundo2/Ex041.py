from datetime import date
nasc = int(input('Em que ano você nasceu? : '))
anoat = date.today().year
id = int(anoat - nasc)
print(f'O atleta tem {id} anos')
if (id <= 9 ):
    print('Sua categoria é : MIRIM')
elif ( id <= 14):
    print('Sua categoria é : INFANTIL')
elif ( id <= 19):
    print('Sua categoria é : JUNIOR')
elif ( id <= 25):
    print('Sua categoria é : SÊNIOR')
else:
    print('Sua categoria é : MASTER')