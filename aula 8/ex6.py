# 6.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# Lista para armazenar as médias
medias = []

# Leitura das notas de 10 alunos
for i in range(5):
    print(f"\nAluno {i+1}:")
    soma = 0
    for j in range(4):
        nota = float(input(f"  Digite a {j+1}ª nota: "))
        soma += nota
    media = soma / 4
    medias.append(media)

# Contagem de alunos com média >= 7.0
aprovados = 0
for media in medias:
    if media >= 7.0:
        aprovados += 1

# Exibição do resultado
print("\nMédias dos alunos:")
for i, media in enumerate(medias, 1):
    print(f"Aluno {i}: média = {media:.2f}")

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {aprovados}")
