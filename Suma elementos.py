import os
os.system('cls' if os.name == 'nt' else 'clear')

lista = []
suma = 0

print("Ingresa 5 numeros:")

for i in range(5):
    num = int(input(f"Numero {i+1}: "))
    lista.append(num)
    suma = suma + num

print("\n--- Resultado ---")
print(f"Tu lista es: {lista}")
print(f"La suma total es: {suma}")