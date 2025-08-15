# Altere o programa anterior para mostrar no final a soma dos números.


while True:
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        break
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

# Determina o início e fim do intervalo
inicio = min(num1, num2) + 1
fim = max(num1, num2)

soma = 0  # Acumulador da soma

print(f"\nNúmeros inteiros entre {num1} e {num2}:")

for i in range(inicio, fim):
    print(i)
    soma += i

print(f"\nSoma dos números do intervalo: {soma}")
