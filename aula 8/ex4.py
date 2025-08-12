# 4.	Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.


caracteres = []
vogais = ['a', 'e', 'i', 'o', 'u']
for i in range(10):
    char = input(f"Digite o {i+1}º caractere: ").lower()
    if len(char) == 1 and char.isalpha():  # Garante que é uma letra única
        caracteres.append(char)
    else:
        print("Entrada inválida. Digite apenas uma letra.")
        exit()
consoantes = [c for c in caracteres if c not in vogais]
print("\nConsoantes digitadas:")
for c in consoantes:
    print(c)

print(f"\nQuantidade de consoantes: {len(consoantes)}")
