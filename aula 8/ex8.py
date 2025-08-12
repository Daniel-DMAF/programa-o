# 8.	Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

# Listas para armazenar as idades e alturas
idades = [20, 30, 40, 50, 60]
alturas = [170, 180, 190, 175, 150]

# Leitura dos dados de 5 pessoas
for i in range(5):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa (em metros): "))
    
    idades.append(idade)
    altura.append(altura)

# Exibição na ordem inversa
print("\nDados na ordem inversa:")

for i in range(4, -1, -1):  # de 4 até 0 (inclusive), indo para trás
    print(f"{5 - i}ª pessoa - Idade: {idades[i]} anos, Altura: {alturas[i]:.2f} m")

