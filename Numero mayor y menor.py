nums = []

print("Mete 8 numeros:")

for i in range(8):
    n = int(input(f"Numero {i+1}: "))
    nums.append(n)

mayor = nums[0]
menor = nums[0]

for valor in nums:
    if valor > mayor:
        mayor = valor
    if valor < menor:
        menor = valor

print("\n--- Resultado ---")
print(f"Lista: {nums}")
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")