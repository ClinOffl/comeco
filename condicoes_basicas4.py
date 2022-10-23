#  Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
# BISSEXTO.

ano = int(input(f'Digite um ano:'))

if ano % 4 ==0:
    print(f'Bissexto')
else:
    print(f'Não é bissexto')
