import os
os.system('cls' if os.name == 'nt' else 'clear')

# programa para contar pares e impares
numeros = []
pares = 0
impares = 0

print("Mete 10 numeros:")

for i in range(10):
    n = int(input(f"Numero {i+1}: "))
    numeros.append(n)
    
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("\n--- Resultados ---")
print(f"Lista que metiste: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")