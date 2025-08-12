lista = []
for i in range(4):
    notas = float(input(f'Digite aqui o valor das {i+1}º notas: '))
    lista.append(notas)
print(f'A sua lista de notas é {lista}')

media = sum(lista) / len(lista)
print(f'A média das notas é {media}')
    