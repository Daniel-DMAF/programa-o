# 5.	Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


numeros = []
pares = []
impares = []

for i in range(20):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("\nTodos os números digitados:")
print(numeros)

print("\nNúmeros pares:")
print(pares)

print("\nNúmeros ímpares:")
print(impares)

