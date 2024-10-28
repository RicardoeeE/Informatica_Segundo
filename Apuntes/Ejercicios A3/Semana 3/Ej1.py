n=int(input("Dame un numero positivo menor que 100: "))
while n<0 or n>100:
    print("Error introduce de nuevo el numero")
    n=int(input("Dame un numero positivo menor que 100: "))

columna_1=[]    
columna_2=[]

i=1
while i <=n:
    # print(i)
    columna_1.append(i)
    i=i+1

e=2*n
while e>=2:
    # print(e)
    columna_2.append(e)
    e=e-2

for valor in columna_1:
    print(valor)

for valor in columna_2:
    print(valor)

#### USANDO EL METODO ZIP
# for valor1,valor2 in zip(columna_1, columna_2):
#     if valor1<valor2:
#         print("(-)")
#     elif valor1>valor2:
#         print("(+)")
#     else:
#         print("Error no capturado")

# Aqui se crea una secuencia de numeros para darles ids a 
# cada valor de la columna_1 al tener la misma longitud que columna_2
# se va comprando elemento a elemento
for i in range(len(columna_1)):
    if columna_1[i] < columna_2[i]:
        print("(-)")
    elif columna_1[i] > columna_2[i]:
        print("(+)")
    else:
        print("Error no capturado")
