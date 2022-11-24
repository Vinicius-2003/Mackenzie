simbolos = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','@','#']
palavra = input('Escreva a palavra a ser incriptada : ').lower()
chave = int(input('Insira a chave : '))
i = 0 
while (i < len(palavra)):
    posicao = simbolos.index(palavra[i])
    nova_posicao = (posicao - chave) % len(simbolos)
    print(simbolos[nova_posicao],end='')
    i = i + 1
