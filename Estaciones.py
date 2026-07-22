#Las estaciones del año match case (Juan Diego Almanza Veloz)
mes = int(input("Ingrese el número del mes (1-12): "))

match mes:
    case 12 | 1 | 2:
        estacion = "Invierno"
    case 3 | 4 | 5:
        estacion = "Primavera"
    case 6 | 7 | 8:
        estacion = "Verano"
    case 9 | 10 | 11:
        estacion = "Otoño"
    case _:
        estacion = "No hay ese mes"

print("La estación del año es:", estacion)
