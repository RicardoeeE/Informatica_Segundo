n=int(input("Dame un numero mayor que cero: "))
while n<0:
    print("ERROR")
    n=int(input("Dame un numero mayor que cero: "))

# Calcular factorial:
i=1
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial,i)