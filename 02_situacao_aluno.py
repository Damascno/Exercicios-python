nota_1 = float(input('Digite a nota: '))
nota_2 = float(input('Digite a nota: '))

media = (nota_1 + nota_2) / 2

print(f'Sua média é: {media:.2f}')

if media >= 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print(f'Situação: {situacao}')
