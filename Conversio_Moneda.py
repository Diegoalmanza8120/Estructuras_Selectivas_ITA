#Conversion de dineros(Juan Diego Almanza Veloz)
money = float(input("Ingrese la cantidad de dinero en pesos mexicanos MXN: $"))
print("Seleccione una opción para convertir el dinero:")
print("1.- USD 2.- EUR 3.-TBH 4.- JPY 5.-KRW 6.- AUD 7.- PEN 8.- CAD 9.- VES 10.- ARS")
opcion = int(input("Ingrese la opción deseada : "))
match opcion:
    case 1:
        resultado = money / 17.40
        unidad ="USD (Dolares Estadounidenses)"
    case 2:
        resultado = money / 19.85 
        unidad ="EUR (Euros)"
    case 3:
        resultado = money / 0.52    
        unidad ="TBH (Thailand Baht)"
    case 4:
        resultado = money / 0.11    
        unidad ="JPY (Yenes Japoneses)"
    case 5:   
        resultado = money / 0.00117
        unidad ="KRW (Won Coreano)"
    case 6:
        resultado = money / 12.19
        unidad ="AUD (Dolares Australianos)"
    case 7:
        resultado = money / 5.12
        unidad ="PEN (Soles Peruanos)"
    case 8:
        resultado = money / 12.34
        unidad ="CAD (Dolares Canadienses)"
    case 9:
        resultado = money / 0.0023
        unidad ="VES (Bolivares Venezolanos)"
    case 10:
        resultado = money / 0.012
        unidad ="ARS (Pesos Argentinos)"
    case _:
        print("Opción no válida")

if opcion in range(1, 11):
    print("La cantidad de dinero en", unidad, "es:", resultado)