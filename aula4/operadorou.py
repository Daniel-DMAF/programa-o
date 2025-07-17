dinheiro = True
senha = True
if dinheiro == True and senha == True:
    print('saque')
elif dinheiro == True and senha == False:
    print('saldo insuficiente')
elif dinheiro == False and senha == True:
    print('Saldo insuficiente')
elif dinheiro == False and senha == False:
    print('saldo e senha inválidos')