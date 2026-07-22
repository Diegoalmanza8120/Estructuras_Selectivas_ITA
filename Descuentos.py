#Calculo de descuentos (Juan Diego Almanza Veloz)

precio = float(input("Ingrese el precio del producto o compra: "))
if precio <= 100:
    descuento = 0.05
elif precio <= 200:
    descuento = 0.10
elif precio <= 500:
    descuento = 0.15
else:
    descuento = 0.20

precio_final = precio - (precio * descuento)

print("Descuento aplicado:", descuento * 100, "%")
print("Precio final:", precio_final)