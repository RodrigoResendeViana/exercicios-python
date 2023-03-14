preco = float(input('Digite o preco do produto: '))
desconto = preco * 0.10
preco_final = preco - desconto
print(f'Desconto {desconto}')
print(f'O preço final do seu produto com 10% de desconto é {preco_final}')