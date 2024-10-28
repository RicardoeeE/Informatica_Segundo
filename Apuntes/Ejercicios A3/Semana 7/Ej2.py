n = int(input("Introduce la dimensión de los vectores (un número entero positivo menor que 30): "))

while n <= 0 or n >= 30:
    print("Error: la dimensión debe ser un entero positivo menor que 30.")
    n = int(input("Introduce la dimensión de los vectores: "))

vector1 = []
for i in range(n):
    valor = float(input(f"Introduce el valor {i+1} para el primer vector: "))
    vector1.append(valor)

vector2 = []
for i in range(n):
    valor = float(input(f"Introduce el valor {i+1} para el segundo vector: "))
    vector2.append(valor)

producto_escalar = sum(vector1[i] * vector2[i] for i in range(n))

print(f"El producto escalar de los dos vectores es: {producto_escalar:.2f}")
