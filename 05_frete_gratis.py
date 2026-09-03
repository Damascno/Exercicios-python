valor = float(input('Valor da compra: '))

if valor >= 100:
    situacao = 'Você ganhou frete grátis!'
else:
    situacao = 'Frete será cobrado.'

print(f'{situacao}')
