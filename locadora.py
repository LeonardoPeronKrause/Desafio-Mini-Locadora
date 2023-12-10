dias = int(input('Digite a quantidade de dias que você alugou o carro: '))

km = float(input('Digite a quantidade de km rodados com esse carro: '))

preco = (dias * 60) + (km * 0.15)

print('Você ficou \033[1;34m{}\033[m dias com o carro, e rodou \033[1;33m{}\033[m KM, o valor a pagar é de R$\033[1;31m{:.2f}\033[m'.format(dias, km, preco))