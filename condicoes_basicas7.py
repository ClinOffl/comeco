# Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
# viagens até 200Km e R$0.45 para viagens mais longas.

distancia = int(input(f'Qual distância deseja percorrer?:'))

passagem = (0.50 * distancia)
passagem1 = (0.45 * distancia)
if distancia > 200:
    print(f'Será cobrado R${passagem1} por essa viagem!')

elif distancia < 200:
    print(f'Será cobrado R${passagem} por essa viagem!')



