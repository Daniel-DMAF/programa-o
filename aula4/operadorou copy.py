dinheiro = True
senha = True

if dinheiro and senha:
    print('Saque realizado com sucesso')
elif dinheiro and not senha:
    print('Senha incorreta')
elif not dinheiro and senha:
    print('Saldo insuficiente')
elif not dinheiro and not senha:
    print('Saldo insuficiente e senha incorreta')