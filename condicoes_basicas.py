# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
# o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

vel = int(input('Qual a velocidade do carro:'))

if vel > 80:
    print(f'Você será multado pelo limite de velocidade de 80km/h!')

multa = vel * 5
print(f'O valor da multa é de: R${multa}')

input()


