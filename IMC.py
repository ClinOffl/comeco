
massa = float(input('Digite seu peso:'))

altura = float(input('Digite sua altura. (ex 1.70):'))

imc = float( massa / (altura**2))

print(f'Seu IMC é: {imc}')

if imc >= 18.5 and imc < 25:
    print('Parabéns, você está no peso ideal!')

if imc < 17:
    print('Muito abaixo do peso')

if imc > 17 and imc < 18:
    print('Abaixo do peso')

if imc > 25 and imc <= 30:
    print('Sobrepeso')

if imc > 30 and imc <= 35:
    print('Obesidade')

if imc > 35 and imc <=40:
    print('Obesidade Severa')

if imc > 40:
    print('Obesidade Mórbida')







