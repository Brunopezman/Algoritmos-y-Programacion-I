# Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo de examenes.
# - En cada paso debe preguntar la cantidad de ejercicios resueltos por el alumno, indicando con un valor centinela que no hay más examenes a revisar. 
# - Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

def notas():
    
    examenes = 'SI'

    while examenes != 'NO':

        ejercicios = int(input('Indique la cantidad de ejercicios del examen: '))
        ej_resueltos = int(input('Indique la cantidad de ejercicios que resolvio el alumno: '))

        if ej_resueltos >= 0.6 * ejercicios:
            print(f"Aprobado. Ejercicios resueltos: {ej_resueltos}")
        else:
            print(f"Desaprobado. Ejercicios resueltos: {ej_resueltos}")
    
        examenes = input('Le quedan examenes para corregir: ').upper()
    

notas()


