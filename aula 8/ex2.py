# 2.	Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

# Lista para armazenar os 10 números reais
numeros = []

# Leitura dos 10 números reais
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

# Exibição dos números na ordem inversa
print("\nNúmeros na ordem inversa:")
for numero in reversed(numeros):
    print(numero)
