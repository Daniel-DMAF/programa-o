

while True:
    try:
        base = float(input("Digite a base: "))
        expoente = int(input("Digite o expoente (inteiro não negativo): "))
        if expoente < 0:
            print("Por favor, digite um expoente inteiro não negativo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Digite números válidos.")

resultado = 1
for _ in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} é {resultado}")