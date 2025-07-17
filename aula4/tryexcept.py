
try:
    numero = int(input('digite um número'))
    
    if(numero %2 == 0):
        print("par")
    else:
        print()
    


except ValueError:
    print('Deu ruim... Você não digitou um número inteiro.')