#Calculadora de calificaciones (Juan Diego Almanza Veloz)

parciales = float(input("Calificación de parciales: "))
proyecto = float(input("Calificación del proyecto: "))
examen = float(input("Calificación del examen: "))

if(parciales <0 or parciales> 100) or (proyecto <0 or proyecto> 100) or (examen <0 or examen> 100):
    print("Error: Las calificaciones deben estar entre 0 y 100.")
else:
    calificacion_final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)
    print("La calificación final es: ", calificacion_final)
