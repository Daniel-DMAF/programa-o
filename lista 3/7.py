#Faça um programa que leia 5 números e informe a soma e a média dos números.


soma = 0

for i in range(1, 6):
    while True:
        try:
            numero = float(input(f"Digite o {i}º número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    soma += numero

media = soma / 5

print(f"\nSoma dos números: {soma}")
print(f"Média dos números: {media}")
