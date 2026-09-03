senha = input('Digite sua senha: ')

if senha == '1234':
    situacao = 'Acesso permitido'
else:
    situacao = 'Senha incorreta'

print(f'{situacao}')
