# 3.	Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# Lista para armazenar as notas
notas = []

# Leitura das 4 notas
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Cálculo da média
media = sum(notas) / len(notas)

# Exibição das notas
print("\nNotas digitadas:")
for i, nota in enumerate(notas, 1):
    print(f"Nota {i}: {nota}")

# Exibição da média
print(f"\nMédia das notas: {media:.2f}")
