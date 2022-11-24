num = int(input('Digite um número : '))
print('''Opções de Conversão :
[1]: Binário
[2]: Octal
[3]:Hexadecimal''')
conv = int(input('Qual base deseja escolher? : '))
if conv == 1:
    print('O número {} em BINÁRIO é {} '.format(num,bin(num)[2:]))
elif conv == 2 :
    print('O número {} em OCTAL é {} '.format(num,oct(num)[2:]))
elif conv ==3:
    print('O número {} em Hexadecimal é {} '.format(num,hex(num)[2:]))
else:
    print('\033[1;32mEscolha inválida!\033[m')