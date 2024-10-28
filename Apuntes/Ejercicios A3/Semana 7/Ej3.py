f = input("Introduce una frase: ")
c = input("Introduce un carácter: ")

vocales = "aeiouAEIOU"
for vocal in vocales:
    f = f.replace(vocal, c)

print(f)
