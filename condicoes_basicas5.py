# Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
# situação em relação ao alistamento militar.
#  - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
# alistamento.
#  - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
# alistamento.

from datetime import date

atual = date.today().year

nasc = int(input(f'Qual o seu ano de nascimento:'))
idade = atual - nasc

print(f'Quem nasceu em {nasc} hoje tem: {idade} anos em {atual}!')
if idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento!')

elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')







