idade = int(input('Digite sua idade: '))
nota = float(input('Digite sua nota: '))

if idade >= 18 and nota >= 6:
    situacao = 'Aprovado!'
else:
    situacao = 'Reprovado!'

print(f'{situacao}')
