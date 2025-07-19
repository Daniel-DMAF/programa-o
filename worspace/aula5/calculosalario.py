# Entrada de dados
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Exibição do resultado
print(f"O salário total é: R$ {salario:.2f}")