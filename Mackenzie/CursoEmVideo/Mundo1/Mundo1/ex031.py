dist = float(input('\033[1;34mQual a distância a ser percorrida? : \033[m'))
if (dist <= 200):
    preco = (dist * 0.5)
else:
    preco = (dist * 0.45)
print('\033[1;34mO preço da passagem total será de {:.0f} R$\033[m'.format(preco))