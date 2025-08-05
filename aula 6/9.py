#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


while True:
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        break
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

# Determina os limites do intervalo (menor e maior)
inicio = min(num1, num2) + 1
fim = max(num1, num2)

print(f"\nNúmeros inteiros entre {num1} e {num2}:")

for i in range(inicio, fim):
    print(i)
