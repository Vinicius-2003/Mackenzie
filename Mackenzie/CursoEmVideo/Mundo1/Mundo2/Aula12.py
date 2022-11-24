nome = str(input('\033[1;33mQual o seu nome?\033[m : '))
if (nome == 'Vinicius'):
    print('\033[34mQue nome bonito!\033[m')
elif (nome == 'joão') or (nome == 'maria') or ( nome == 'paulo'):
    print('\033[34mSeu nome é bem comum no Brasil!\033[m')
else:
    print('Seu nome é bem comum!')
print('\033[33mTenha um bom dia , {}!\033[m'.format(nome))