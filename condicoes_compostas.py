#  Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
# na tela uma das mensagens abaixo:
#  - O primeiro valor é o maior
#  - O segundo valor é o maior
#  - Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número:'))
num2 = int(input(f'Digite outro número:'))

if num1 > num2:
    print(f'O {num1} é maior que o {num2}')

elif num2 > num1:
    print(f'O {num2} é maior que o {num1}')

elif num1 == num1:
    print(f'Não existe valor maior pois os dois são iguais!')

