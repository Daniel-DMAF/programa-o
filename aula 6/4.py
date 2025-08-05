# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    try:
        # Entrada da população A
        while True:
            pop_a = int(input("Informe a população do país A: "))
            if pop_a > 0:
                break
            print("População deve ser maior que zero.")

        # Entrada da população B
        while True:
            pop_b = int(input("Informe a população do país B: "))
            if pop_b > 0:
                break
            print("População deve ser maior que zero.")

        # Entrada da taxa de crescimento A
        while True:
            taxa_a = float(input("Informe a taxa de crescimento anual do país A (em %): "))
            if taxa_a > 0:
                break
            print("A taxa deve ser maior que zero.")

        # Entrada da taxa de crescimento B
        while True:
            taxa_b = float(input("Informe a taxa de crescimento anual do país B (em %): "))
            if taxa_b > 0:
                break
            print("A taxa deve ser maior que zero.")

        # Cálculo dos anos necessários
        anos = 0
        pop_atual_a = pop_a
        pop_atual_b = pop_b

        # Verifica se A já é maior
        if pop_a >= pop_b:
            print("A população do país A já é maior ou igual à do país B.")
        else:
            while pop_atual_a <= pop_atual_b:
                pop_atual_a += pop_atual_a * (taxa_a / 100)
                pop_atual_b += pop_atual_b * (taxa_b / 100)
                anos += 1

            print(f"\nSerá necessário {anos} anos para que a população do país A ultrapasse ou iguale a do país B.")
            print(f"População A: {int(pop_atual_a)}")
            print(f"População B: {int(pop_atual_b)}")

    except ValueError:
        print("Erro de entrada. Por favor, digite números válidos.")

    # Deseja repetir?
    repetir = input("\nDeseja fazer outra simulação? (s/n): ").strip().lower()
    if repetir != 's':
        print("Programa encerrado.")
        break
