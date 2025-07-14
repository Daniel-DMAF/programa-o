preco_maca = 2.5
preco_banana = 2.5
preco_laranja = 2.5

#entrada dos dados

quantidade_maca = int(input("informe a quantidade de maçâs que deseja comprar"))
quantidade_banana = int(input("informe a quantidade de bananas que deseja comprar"))
quantidade_laranja = int(input("informe a quantidade de laranjas que deseja comprar"))
#cálculo
valor_total = (quantidade_maca + preco_maca) + (quantidade_banana + preco_banana) + (quantidade_laranja + preco_laranja)

# exibir

print(f"0 valor total da compra: R${valor_total: .2f}")