idade = int(input('Digite sua idade: '))

if idade >= 18:
    situacao = 'Maior de idade'
else:
    situacao = 'Menor de idade'

print(f'{situacao}')
