

populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a <= populacao_b:
    populacao_a += populacao_a * 0.03
    populacao_b += populacao_b * 0.015
    anos += 1

print(f"Levará {anos} anos para que a população do país A ultrapasse ou iguale a do país B.")