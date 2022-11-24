nome = str(input('Qual o nome do cliente? : '))
regiao = int(input('Digite o código da região: '))
peca = int(input('digite o número de peças vendidas : '))
nomevend = str(input('Me informe o nome do vendedor : '))
frete = 0
custototal= peca * 7
valordevenda = custototal * 1.5
comissãovend = +((valordevenda*6.5)/100)
lucro = valordevenda - custototal - comissãovend
if regiao == 1:
    if (peca <= 1000):
        frete = peca * 1.00
    else:
        frete = peca * 0.9
if regiao == 2:
    if (peca <= 1000):
        frete = peca * 1.10
    else:
        frete = peca * 1.0
if regiao == 3:
    if (peca <= 1000):
        frete = peca * 1.15
    else:
        frete = peca * 1.10
if regiao == 4:
    if (peca <= 1000):
        frete = peca * 1.20
    else:
        frete= peca * 1.15
print(f'O valor do frete de entrega será de {frete}R$')
print(f'A comissão paga ao vendedor será de {comissãovend}R$')
print(f'O lucro da venda foi de {lucro}R$')