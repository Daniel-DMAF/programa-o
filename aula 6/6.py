# Faça um programa que leia 5 números e informe o maior número.


maior = None  # Inicializa a variável que guardará o maior número

for i in range(1, 6):
    while True:
        try:
            numero = float(input(f"Digite o {i}º número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    if (maior is None) or (numero > maior):
        maior = numero

print(f"\nO maior número digitado foi: {maior}")
