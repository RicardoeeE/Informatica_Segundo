n=int(input("Dame un numero entero postivo: " ))
while n<0:
    print("ERROR")
    n=int(input("Dame un numero entero postivo: " ))
i=1
lista=[]
for i in range(1,n):
  if n%i==0:
     lista.append(i)
print("Divisiores propios: ", lista)

suma_diviores=sum(lista)
n_str=str(n)
if n==suma_diviores:
   print(n_str+" Es un numero perfecto")
else:
   print("NO es un número perfecto.")