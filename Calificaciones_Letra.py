#Calificaciones con letra (Juan Diego Almanza Veloz)

c = float(input("Ingrese la calificación: "))
if c >= 90:
    calificacion = "A"
elif c >= 80:
    calificacion = "B"
elif c >= 70:
    calificacion = "C"
elif c >= 60:
    calificacion = "D"
else:
    calificacion = "F"
print("La calificación es:", calificacion,"Equivale a", c,"puntos")    