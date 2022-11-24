valor = float(input('Qual o valor da casa ? : '))
sal = float(input('Quanto você ganha? : '))
ano = int(input('Em quantos anos deseja pagar? : '))
prest = (valor/(12*ano))
if (prest > (sal*30)/100):
     print('O valor da parcela {:.1f} \n Excede ao valor de seu salário..'.format(prest),end='')
     print('Seu pedido foi \033[1;31mNEGADO\033[m')
else:
    print('\033[1;32mAPROVADO!\033[mVocê deverá pagar mensalmente, {:.1f}R$ ao Banco'.format(prest))