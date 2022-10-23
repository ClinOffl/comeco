'''

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1

(0 a 10)

  - - -- - - - - -  - - -  - - - -

contador = 10

while contador >= 0:
    print(contador)
    contador = contador - 1

(10 a 0)

 - - -- - - - - -  - - -  - - - -

contador = 0

valor = int(input(f'Quer contar até quanto?:'))

while (contador <= valor):

    print(contador)
    contador = contador + 1

(RECEBENDO DADOS DE UM USUARIO)


- - -- - - - - -  - - -  - - - -
contador = 0

valor = int(input(f'Quer contar até quanto?:'))

salto = int(input(f'Qual será o valor do salto:'))

while (contador <= valor):

    print(contador)
    contador = contador + salto

(RECEBENDO DADOS DE UM USUARIO)

cont = 1
soma = 0

while cont <= 5:
    print(f'Digite um valor:')
    numero = int(input())

    soma = soma + numero
    cont = cont + 1

print(f'A soma de todos valores foi: {soma}')

(SOMANDO)

- - -- - - - - -  - - -  - - - -

cont = 1
soma = 0
maior = 0

while cont <= 5:
    num = int(input(f'Digite um valor:'))
    soma = soma + num
    cont = cont + 1
if num > maior:
    maior = num


print(f'A soma de todos valores foi: {soma}')
print(f'O maior número digitado foi: {maior}')

(DESCOBRINDO MAIOR VALOR)

- - -- - - - - -  - - -  - - - -
cont = 1
soma = 0
maior = 0
menor = 0

while cont <= 5:
    num = int(input(f'Digite um valor:'))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma = soma + num
    cont = cont + 1

print(f'A soma de todos valores foi: {soma}')
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')

(MAIOR, MENOR)


- - -- - - - - -  - - -  - - - -

conv = 1
D = 0
quantidade = int(input(f'Quantas vezes deseja converter?'))
while conv <= quantidade:
    real = float(input(f'Qual o valor em R$:'))
    D = real / 5.16
    print(f'O valor convertido em dolar é: {D}')
    conv = conv + 1

(Convertendo dolar quantas vezes precisar)


'''






