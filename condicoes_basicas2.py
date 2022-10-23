# 18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.

nasc = int(input(f'Digite o ano de nascimento:'))

idade = 2022 - nasc

if idade > 16:
    print(f'Você está apto para votar!')
else:
    print('Você não está apto para votar')
