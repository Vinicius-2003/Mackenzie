#Como tirar os espaços entre palavras. 
a = str(input('Digite uma frase : ')).strip().lower()
b = a.split()
c = ''.join(b)
print('a frase escrita e sem espaços é {}'.format(c))

#Detector de palindromo
for a in range(2):
    frase = str(input('frase : ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    n = junto[::-1]
    print(n)
    if (junto== n):
        print('A frase digitada \033[34mÉ\033[m um palíndromo!!')
    else:
        print('A frase \033[31mNÃO\033[m é um palindromo')
