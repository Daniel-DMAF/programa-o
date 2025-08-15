# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# Supondo que a população de um país A seja da ordem de 80000 habitantes 
# com uma taxa anual de crescimento de 3% e que a população de B seja 
# 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa 
# que calcule e escreva o número de anos necessários para que a população 
# do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    print("Nome deve ter mais de 3 caracteres.")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        print("Idade deve estar entre 0 e 150.")
    except ValueError:
        print("Digite um número inteiro válido para a idade.")

while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        print("O salário deve ser maior que zero.")
    except ValueError:
        print("Digite um valor numérico válido para o salário.")

while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
    if sexo in ['f', 'm']:
        break
    print("Sexo deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Digite seu estado civil ('s' - solteiro, 'c' - casado, 'v' - viúvo, 'd' - divorciado): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    print("Estado civil deve ser 's', 'c', 'v' ou 'd'.")


populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a <= populacao_b:
    populacao_a += populacao_a * 0.03
    populacao_b += populacao_b * 0.015
    anos += 1

print(f"Levará {anos} anos para que a população do país A ultrapasse ou iguale a do país B.")