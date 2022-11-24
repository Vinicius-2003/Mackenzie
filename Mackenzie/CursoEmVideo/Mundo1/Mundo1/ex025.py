#Saber se o nome escrito tem Silva nele
nome = str(input('Qual é seu nome completo? : ')).strip()
print('Seu nome tem Silva? : {} '.format('silva' in nome.lower()))

#saber se há algarismo 1 
num =str(input('Número : '))
print('Têm o numro 1? {}'.format('1' in num))