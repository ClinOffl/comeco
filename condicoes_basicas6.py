# Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
# para todos, mas especialmente para mulheres. Faça um programa que leia nome,
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
# que:
#  - Homens ganham 5% de desconto
#  - Mulheres ganham 13% de desconto

nome = input('Digite seu nome:')

sx = int(input('Digite o sexo: (1 PARA HOMEM e 2 PARA MULHER):'))

vi = int(input('Valor da compra R$:'))

vsd = vi * 5 / 100
vsd2 = vi * 13 / 100

if sx == 1:
    print(f'O desconto é de R$ {vsd}')

else:
    print(f'O desconto é de R$ {vsd2}')








