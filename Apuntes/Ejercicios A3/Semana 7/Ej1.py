longitud = int(input("Introduce la dimensión de la lista (MAX 50): "))

while longitud < 1 or longitud > 50:
    print("Error: debe cumplir las condiciones.")
    longitud = int(input("Introduce la dimensión de la lista (MAX 50): "))

lista = []

for i in range(longitud):
    valor = int(input(f"Introduce el valor para la posición {i}: "))
    lista.append(valor)

for pos, value in enumerate(lista):
    print(f"Posición {pos}, valor {value}")

contador_negativos = 0
for i in range(1, len(lista), 2):
    if lista[i] < 0:
        contador_negativos += 1

print("Cantidad de números negativos en posiciones impares:", contador_negativos)
