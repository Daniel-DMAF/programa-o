#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    try:
        nota = float(input('Digite uma nota entre [0 e 10]: '))
        if nota < 0 or nota > 10:
            print('Você digitou um valor fora da faixa.')
        else:
            print('Você digitou um valor válido.')
            break
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")