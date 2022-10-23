# Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
#  - Até 3 anos de empresa: aumento de 3%
#  - entre 3 e 10 anos: aumento de 12.5%
#  - 10 anos ou mais: aumento de 20%

nome = input(f'Digite seu nome:')
sal = int(input(f'Digite seu salário: R$'))
casa = int(input('Tempo de casa:'))

aum3 = sal + (sal * 3 / 100)
aum12 = sal + (sal * 12.5 / 100)
aum20 = sal + (sal * 20 / 100)

if casa == 3:
    print(f'Aumento de 3%, novo salário de: R${aum3}')

elif casa >= 3 and casa <= 10:
    print(f'Aumento de 12.5%, novo salário de: R${aum12}')

elif casa > 10:
    print(f'Aumento de 20%. novo salário de: R${aum20}')








