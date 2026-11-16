import os
os.system('cls' if os.name == 'nt' else 'clear')

lista = []

print("Anota 6 numeros:")

for i in range(6):
    n = int(input(f"Ingresa el numero {i+1}: "))
    lista.append(n)

lista.reverse()

print("\n--- Resultado ---")
print(f"Lista invertida: {lista}")