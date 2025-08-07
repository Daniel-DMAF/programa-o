fruta = ['maçã', 'banana', 'laranja', 'pitaya','mamão']

print(f'Todas as frutas ===>{fruta [4]}')
tamanho = len(fruta)
print(f'O tamanho da lista é {tamanho}')
print('.........')
fruta[1] = 'uva'
print(f'Todas as frutas ===>{fruta}')
fruta.insert(1,'abacaxi')
print(f'lista atualizada ===>{fruta}')

# removendo pelo indice
print(fruta)
fruta.pop(1)
print(fruta)