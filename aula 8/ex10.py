# 10.	Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

# Listas para armazenar os dois vetores de entrada
vetor1 = []
vetor2 = []

# Leitura dos 10 elementos do vetor1
for i in range(10):
    num = int(input(f"Digite o {i+1}º número para o vetor 1: "))
    vetor1.append(num)

# Leitura dos 10 elementos do vetor2
for i in range(10):
    num = int(input(f"Digite o {i+1}º número para o vetor 2: "))
    vetor2.append(num)

# Gerando o terceiro vetor com elementos intercalados
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])  # Adiciona elemento do vetor1
    vetor3.append(vetor2[i])  # Adiciona elemento do vetor2

# Exibindo o vetor resultante
print("\nVetor resultante (intercalado):")
print(vetor3)
