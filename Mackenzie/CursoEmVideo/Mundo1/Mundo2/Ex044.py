preco = float(input('Valor da compra : '))
pag = int(input(''' Formas de pagamento : 
 [1] - dinheiro ou cheque
 [2] - Cartão a vista 
 [3] - Cartão 2x
 [4] - Cartão mais de 2x \n
Escolha : '''))
if (pag == 1 ):
    precof = preco * 0.9
    print('O novo preço será de {:.1f}R$'.format(precof))
elif (pag == 2 ):
    precof = preco * 0.95
    print('O novo preço será de {:.1f}R$'.format(precof))
elif (pag == 3):
    print('Não houve alteração no valor final! O preço se mantem em  {:.1f}R$')
elif( pag == 4):
    n = int(input('Em quantas vezes deseja pagar? : '))
    precof = (preco * 1.20)/n
    print('O novo preço será de {:.1f}R$'.format(precof))
elif( pag > 4):
    print('Opção inválida! Tente Novamente')