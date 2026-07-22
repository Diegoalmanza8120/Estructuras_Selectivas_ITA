#Temperaturas de grados °c a °f y °K (Juan Diego Almanza Veloz)
c = float(input("Ingrese la temperatura en grados Celsius °C: "))
print("Seleccione una opción para convertir la temperatura:")
print("1 para Convertir a grados Fahrenheit °F o 2 para Convertir a grados Kelvin °K")
opcion = int(input("Ingrese la opción deseada : "))

match opcion:
    case 1:
        resultado = (c * 9/5) + 32
        unidad = "°F"
    case 2:
        resultado = c + 273.15
        unidad = "°K"
    case _:
        resultado = None
if resultado is not None:
    print("La temperatura en", unidad, "es:", resultado)