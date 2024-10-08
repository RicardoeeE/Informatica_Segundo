# 9 centimos por epgtina, 8% de descuento superior a 500 unidades, 12% si es mayot a 1000
formato="==========================================="
print(formato)
n_pegatinas=int(input("¿Cuantas pegatinas quieres hacer? "))
if n_pegatinas<=0:
    print("ERROR, debe ser psoitivo mayor que cero")

precio_euros= 0.09
if n_pegatinas< 500:
    coste = n_pegatinas *precio_euros
    costeSTR=str(coste)
    print("El coste es de "+costeSTR)
elif n_pegatinas>=500 and n_pegatinas<1000:
    descuento= 8/100
    coste = (precio_euros - descuento) * n_pegatinas #falta calcular el descuento se aplica mal
    costeSTR=str(coste)
    print("El coste es de "+costeSTR)
elif n_pegatinas>=1000:
    descuento= 12/100
    coste = (n_pegatinas * precio_euros) - descuento
print(formato)
