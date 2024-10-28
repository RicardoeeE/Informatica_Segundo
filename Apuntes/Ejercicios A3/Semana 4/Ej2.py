n=int(input("Dame numeros entreos mayores que 0: "))
while n<=0:
    print("ERROR")
    n=int(input("Dame numeros entreos mayores que 0: "))


for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()