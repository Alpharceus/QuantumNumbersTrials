periodic_table = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
    'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20,
    # Add more elements here as needed
}

def get_quantum_numbers(element_symbol):
    atomic_number = periodic_table[element_symbol]
    n = 1
    remaining_electrons = atomic_number

    while remaining_electrons > 0:
        l_max = n - 1
        for l in range(l_max + 1):
            for ml in range(-l, l + 1):
                remaining_electrons -= 1
                if remaining_electrons == 0:
                    ms = 0.5 if atomic_number % 2 != 0 else -0.5
                    return n, l, ml, ms
        n += 1

element_symbol = input("Enter the element symbol: ")
n, l, ml, ms = get_quantum_numbers(element_symbol)
print(f"Quantum numbers for the last electron in the ground state of {element_symbol}:")
print(f"n: {n}")
print(f"l: {l}")
print(f"m: {ml}")
print(f"ms: {ms}")
