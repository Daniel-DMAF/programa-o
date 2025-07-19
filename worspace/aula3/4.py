#Faça um Programa que peça as 4 notas bimestrais e mostre a média.


nota1 = float(input('digite a 1º nota: '))
nota2 = float(input('digite a 2º nota: '))
nota3 = float(input('digite a 3º nota: '))
nota4 = float(input('digite a 4º nota: '))
# processamento
media = (nota1 + nota2 + nota3 + nota4)/4
#saida
#print('média:' ,media)
print(f'A media foi {media:.2f}')
if media >= 7:
    print('situação Aprovado')
elif media >4 and media <7:
    print ('recuperação')
else:
    print('Aprovado')
    
        