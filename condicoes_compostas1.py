# Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#  - Média até 4.9: REPROVADO
#  - Média entre 5.0 e 6.9: RECUPERAÇÃO
#  - Média 7.0 ou superior: APROVADO

nota = int(input(f'Nota 1:'))
nota2 = int(input(f'Nota 2:'))

final = nota + nota2 / 2

if final <= 4.9:
    print('REPROVADO')

elif final == 5.0 and 6.9:
    print(f'RECUPERAÇÃO')

elif final >= 7.0:
    print(f'APROVADO')


