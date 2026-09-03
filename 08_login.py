nome = input('Nome do usuário: ')
senha = input('Digite sua senha: ')

if nome == 'admin' and senha == '1234':
    situacao = 'Login realizado com sucesso!'
else:
    situacao = 'Usuário ou senha incorretos.'

print(f'{situacao}')
