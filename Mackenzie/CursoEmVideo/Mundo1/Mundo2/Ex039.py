from datetime import date
ano = int(input('Em que ano você nasceu : '))
anoat = int(date.today().year) 
s = (anoat - ano)
if (s <= 17):
    print('Você ainda deve se alistar')
    tempo = int(18 - s )
    print('Faltam {} ano(s) para você se alistar!'.format(tempo),end='')
    x = (18 - s) + anoat
    print(' Você deverá se alistar em \033[1;32m{}\033[m '.format(x))
elif ( s == 18):
    print('Está na hora de se alistar!')
elif ( s > 18):
    print('Você já passou do tempo de se alistar!')
    tempo = int(s - 18)
    print('Já faz {} ano(s) que passou do seu alistamento!'.format(tempo),end='')
    y = int(anoat- (s - 18)) 
    print('Seu alistamento foi em \033[1;32m{}\033[m'.format(y))
