n=int(input("Dame un numero mayor que 0 y menor que 10: "))
while n<0 or n>10:
    print("ERROR")
    n=int(input("Dame un numero mayor que 0 y menor que 10: "))
lista=[]

def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial

superfactorial=1
for i in range(1,n+1):
    superfactorial=superfactorial*factorial(i)
print(superfactorial)