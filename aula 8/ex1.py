# 1.	Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# Criando uma lista vazia para armazenar os números
numeros = []

# Lendo 5 números inteiros do usuário
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Exibindo os números digitados
print("\nOs números digitados foram:")
for numero in numeros:
    print(numero)
