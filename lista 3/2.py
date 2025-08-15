#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    
      nome = input('digite o nome')
      senha = input('digite a senha')
      if senha == nome:
          print('você digitou a senha igual ao nome')
      else:
        print('você acertou')
        break
