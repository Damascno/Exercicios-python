idade = int(input('Digite sua idade: '))
ingresso = input('Você possui ingresso? ')

if idade >= 18 and ingresso == 'sim':
    situacao = 'Entrada permitida!'
else:
    situacao = 'Entrada não permitida!'

print(f'{situacao}')
