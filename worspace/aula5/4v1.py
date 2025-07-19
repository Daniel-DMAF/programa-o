# 4 verificar se a letra é vogal ou consoante.

letra = input('Digite uma letra: => ')
letra = letra.upper() #função passa maiusculo
vogal =['A', 'E', 'I', 'O', 'U']
consoante = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'M', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'W', 'Z']

if letra in vogal:
    print('A letra é uma vogal')
elif letra in consoante:
    print('A letra é uma consoante')
else:
    print('O caracter digitado não é uma letra')