#facça um programa que pergunte, quanto você ganha por horas, trabalhadas no mê. calcule e mostre o total do salario referido.

#entreda

valor_hora = float(input('Quanto você ganha por hora?'))
horas_trabalhadas = float(input('Quantas horas você trabalhou no mês?'))
salario = valor_hora * horas_trabalhadas
print(f'Seu salário no mês é: R$ {salario:.2f}')

#processamento