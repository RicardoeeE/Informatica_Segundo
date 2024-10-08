num=int(input("Dame un numero entero de 3 cifras: "))
if num<99 and num>999:
    print("Error, el numero debe tener 3 cifras")
else:  
    centenas = num // 100         
    decenas = (num % 100) // 10  
    unidades = num % 10           
    # print(centenas,decenas,unidades)
    # Comprobar capicua:
    if centenas == unidades:
        print("El numero es capicua")
    else:
        print("Ese no lo es, prueba uno disitnto")