#Números do intervalo de 50 a 100

count = 50
while count <= 100:
    print(count)
    count=count+1 
print('Esses são os números do intervalo de 50 a 100')

#Contagem regressiva

count = 10
while count >= 0:
    print(count)
    count = count-1
print('Fogo!')

#Soma de 5 valores aleatórios

conta = 0
total = 0
while conta <= 5 :
    x = int(input('Me fale um valor : '))
    conta=conta+1
    total = total + x
print(f'O total da soma dos valores escolhidos é {total}!')

#10 primeiros multiplos de 3

x = 0
count = 0
print(f'Os primeiros 10 multiplos de 3 são : ')
while count <= 10:
    tab = 3 * x
    x = x + 1
    print(tab)
    count= count + 1

#Saber se um número é primo:

count = 0
num = int(input('Me fale um numero : '))
while count <= 5:
    if (num % 2 == 0) or (num % 3 == 0):
        print('Não é primo')
        count = count  + 1
        num = int(input('Me fale um numero : '))
    else:
        print('É primo!')
        count = count + 1 
        num = int(input('Me fale um numero : '))


#Soma dos 10 primeiros números Inteiros


count = 0
total = 0
while count < 10 :
    num = int(input('Me fale um numero inteiro : '))
    count += 1
    total = total + num       
print(total)


#Média de uma aluno.

count = 0
alunos = int(input('Me fale o número de alunos : '))
media = 0 
while count < alunos:
    p1 = float(input('Nota da p1 : '))
    p2 = float(input('Nota da p2 : '))
    count += 1
    media = (p1 + p2)/2
    if media > 7.0:
        print(media)
        print('Aprovado Direto !!')
    else:
        print(media)
        print('Reprovado :( ')


#Média geral de uma turma.

count = 0 
alunos = 0
total = 0 
media = 0
alunos = int(input('Qual o número de alunos : '))
while count < alunos :
    p1 = float(input('Nota p1 : '))
    p2 = float(input('Nota p2 : '))
    count += 1 
    media = (p1 + p2)/2
    total = total + media
    if media >= 7.0:
        print(media)
        print('Aprovado direto!!')
    else:
        print(media)
        print('Reprovado :( ')
total = (total/alunos)
print('A média da turma foi {:.1f}'.format(total))


#Pesquisa realizada com a população.

menor = 0 
maior = 0
menorvalor = 300
acum1 = 0
acum2 = 0
count = 0
while True:
    anos = int(input('Quantos anos você têm : '))
    if anos == -1:
        break
    sexo = input('Qual o seu sexo (M-masculino/ F-feminino): ').upper() 
    if anos > maior:
        maior = anos
    if anos < menorvalor:
        menor = anos
        menorvalor = anos
    if sexo == 'F' and (anos >= 18 and anos <= 35):
        acum1 += 1
    if anos >= 65:
        acum2 += 1
    count += 1
porcenhomens = ((acum2*100)/count)
porcmulheres = ((acum1 * 100)/count)
print(maior)
print(menor)
print(porcmulheres)
print(porcenhomens)