mat = [[0,0,0],[0,0,0],[0,0,0]]
trans = [[0,0,0],[0,0,0],[0,0,0]]

print("Anota matriz 3x3:")
for i in range(3):
    for j in range(3):
        mat[i][j] = int(input("Ingresa un numero: "))

for i in range(3):
    for j in range(3):
        trans[j][i] = mat[i][j]

print("\nMatriz original:")
for fila in mat:
    print(fila)

print("\nMatriz transpuesta:")
for fila in trans:
    print(fila)