import random
from time import sleep
print(f'VAMOS JOGAR PEDRA, PAPEL OU TESOURA?')
print(F'(PEDRA = 1), (PAPEL = 2), (TESOURA = 3)')

esc = int(input('FAÇA SUA ESCOLHA:'))

maquina = random.randint(1, 3)

print(f'O COMPUTADOR JOGOU {maquina}')

if esc == maquina:
    print('EMPATE!')

elif (esc == 1 and maquina == 3) or (esc == 3 and maquina == 2) or (esc == 2 and maquina == 1):
    print(f'VOCÊ VENCEU!')

else:
    print(f'A MAQUINA VENCEU!')

    sleep(6)

