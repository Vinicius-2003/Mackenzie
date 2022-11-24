import math

#exercico para saber se um número é par

num = int(input('Me fale um número inteiro : '))
if num % 2 == 0:
    print('Este número é Par!')
else:
    print('Este número é Impar!')


#exercico de algoritmo 

valor = float(input('Me fale o valor do produto : '))
if valor <= 20.00:
    valor1 = valor + ((valor * 45)/100)
    print('O valor do produto será de {:.1f}R$'.format(valor1))
else:
    valor2 = valor + (valor * 30 )/100
    print('Logo, o valor será de {:.1f}R$'.format(valor2))


#exercicio da prova

vel = float(input('Me fale o valor da velocidade : '))
Convel = str(input('Me fale em qual unidade (m/s ou km/h) : '))
if Convel == 'm/s':
    vel = (vel * 3.6)
    print('Sua velocidade será {:.0f}km/h'.format(vel))
if Convel == 'km/h':
    vel = (vel)/3.6
    print('A sua velocidade será de {:.0f}m/s'.format(vel))


#problema de algoritmo

a = int(input(' Me fale um número : '))
if a >= 0 and a == 0:
    b = math.sqrt(a,2)
    print('a raiz quadrada do seu número é {:.1f}'.format(b))
if a < 0:
    c = math.pow(a,2)
    print('o quadrado do seu número é {:.1f}'.format(c))

a = int(input(' Me fale um número : '))
if ((a >= 0) or (a == 0)):
    a = math.sqrt(a)
    print('a raiz quadrada do seu número é {:.0f}'.format(a))
if (a < 0):
    a = math.pow(a,2)
    print('o quadrado do seu número é {:.0f}'.format(a))



#problema de diferença entre números
 
a = float(input('Me fale um número : '))
b = float(input('me fale outro número : '))
if a > b:
    c = (a - b)
    print('O resultado da subtração do maior pelo menor é {:.1f}'.format(c))
if b > a:
    c = (b - a)
    print('O resultado da subtração do maior pelo menor é {:.1f}'.format(c))



#problema de média
  
n1 = float(input('Me fale a sua primeira nota : '))
n2 = float(input('Me fale o resultado da sua segunda prova : '))
n3 = float(input('Me fale o valor da sua terceira prova : '))
med = ((n1 * 2) + (n2 * 3) + (n3 * 5))/(2+3+5)
print('A sua média está em {:.1f}'.format(med))
if med >= 6:
    print('O aluno está aprovado ! :)')
else:
    print('O Aluno está reprovado ! :(')

#problema do peixe 

peso = int(input('Peso de hoje (em kg) : '))
if peso > 50:
    pesoex = (peso - 50)
    multa = ((peso - 50) * 4)
    print('Visto que seu carregamento excedeu a lei em {:.0f}kg, sua multa hoje será de {:.2f}R$'.format(pesoex,multa))
else:
    print('Seu carregamento está dentro do regulamento!')
