# 1 Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('Digit o primeiro número: '))
n2 = float(input('Digit o segundo número: '))

if n1 > n2:
    print(f'O maior número é: {n1}')
elif n2 > n1:
    print(f'O maior número é: {n2}')
else:
    print('Os doi números são iguais.')
