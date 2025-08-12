# 7.	Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


# Lista para armazenar os números
numeros = []

# Leitura dos 5 números inteiros
for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

# Cálculo da soma
soma = sum(numeros)

# Cálculo da multiplicação
multiplicacao = 1
for num in numeros:
    multiplicacao *= num

# Exibição dos resultados
print("\nNúmeros digitados:")
print(numeros)

print(f"\nSoma dos números: {soma}")
print(f"Multiplicação dos números: {multiplicacao}")
