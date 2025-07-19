# 4 verificar se a letra é vogal ou consoante.

letra = input('Digite uma letra: ').lower()

if letra in 'aeiou':
    print('Vogal')
else:
    print('Consoante')