# Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. 

def dia_de_semana(dia_anio):
    
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    dias_pasados = (dia_anio - 1) % 7
    dia_correspondiente = dias_semana[dias_pasados]

    return print(dia_correspondiente)

dia_de_semana(9)
