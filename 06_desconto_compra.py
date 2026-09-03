valor = float(input('Valor da compra: '))

if valor >= 200:
    desconto = valor * 0.10
    valor_final = valor - desconto
    situacao = 'Você ganhou 10% de desconto!'
else:
    desconto = 0
    valor_final = valor
    situacao = 'Sem desconto!'

print(f'{situacao}')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Valor final: R$ {valor_final:.2f}')
