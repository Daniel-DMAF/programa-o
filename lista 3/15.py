# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

while True:
    try:
        n = int(input("Digite quantos termos da série de Fibonacci você quer ver (n > 0): "))
        if n <= 0:
            print("Digite um número maior que zero.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# Inicializa os dois primeiros termos da série
fib = [1, 1]

# Se o usuário quiser só 1 termo, já mostramos só um
if n == 1:
    print("Série de Fibonacci:")
    print(1)
else:
    # Gera os termos restantes (a partir do 3º)
    for i in range(2, n):
        proximo = fib[i-1] + fib[i-2]
        fib.append(proximo)

    print("Série de Fibonacci:")
    print(', '.join(str(num) for num in fib))
