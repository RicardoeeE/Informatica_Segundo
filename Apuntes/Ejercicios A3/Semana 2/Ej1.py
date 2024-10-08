formato="========================================"
print(formato)
peso=float(input("Introduce tu peso en kg: "))
altura =float(input("Introduce tu altura en metros: "))

imc=peso/(altura*altura)
imcS=str(imc)
if  altura <= 0.0:
    print("La altura ha de ser mayor de cero")
if peso <= 0.0:
    print("La altura ha de ser mayor de cero")

    
if imc < 18.5:
    print("Tu índice de masa corporal es de: "+imcS)
    print("Tienes bajo el peso")
elif imc> 18.5 and imc<24.99:
    print("Tu índice de masa corporal es de: "+imcS)
    print("Tienes un peso normal")
elif imc >25.0 and imc<29.99:
    print("Tu índice de masa corporal es de: "+imcS)
    print("Tienes sobrepeso")
elif imc>=30.0:
    print("Tu índice de masa corporal es de: "+imcS)
    print("Tienes obesidad")

print(formato)
