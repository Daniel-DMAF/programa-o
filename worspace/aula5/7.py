# Maior e menor de três números.

nums = [float(input(f'Digite o {i+1}° número: ')) for i in range(3)]
print(f'Maior: {max(nums)}, Menor: {min(nums)}')