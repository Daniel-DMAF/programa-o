# 9.	Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

# Lista para armazenar os números inteiros
A = []

# Leitura dos 10 números inteiros
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    A.append(num)

# Cálculo da soma dos quadrados
soma_quadrados = sum([num ** 2 for num in A])

# Exibição do resultado
print(f"\nA soma dos quadrados dos elementos do vetor A é: {soma_quadrados}")
