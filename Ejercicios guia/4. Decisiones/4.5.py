# Escribir funciones que resuelvan los siguientes problemas:
# - Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
# - Dado un mes y un año, devolver la cantidad de días correspondientes.
# - Dada una fecha (día, mes, año), indicar si es válida o no.
# - Dada una fecha, indicar los días que faltan hasta fin de mes
# - Dada una fecha, indicar los días que faltan hasta fin de año.
# - Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
# - Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.

dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def es_bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or (anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0):
        return 'Es bisiesto'
    else:
        return 'No es bisiesto'
    
def cantidad_dias_del_anio(mes,anio):

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
       return 30
    elif mes == 2:
        if es_bisiesto(anio) == True:
            return 29
        else:
           return 28
    else:
        return 31


def fecha_valida(dia,mes,anio):

    while dia < 1 or dia > dias_por_mes[mes]:
        print('Dia invalido')
        dia = int(input("introduzca un dia válido: "))

    while mes == 2 and dia >= 30:
        print('Dia invalido')
        dia = int(input("introduzca un dia válido: "))

    while dia == 29 and es_bisiesto(anio) != True:
        print('Dia invalido')
        dia = int(input("introduzca un dia válido: "))

    return 'La fecha es válida'

def dias_para_fin_de_mes(dia, mes, anio):

    cantidad_dias_mes = cantidad_dias_del_anio(mes, anio)
    dias_que_faltan = cantidad_dias_mes - dia

    return dias_que_faltan 

def dias_para_fin_de_anio(dia, mes, anio):

    if es_bisiesto(anio) == True:
        dias_por_mes[3] = 29
        dias_faltantes_fin_de_anio = 366 - ((sum(dias_por_mes[:mes])) + dia) # sum(lista[:posicion]) suma de todos los numeros que componen la lista hasta la posicion pedida sin incluir.
    else:
        dias_faltantes_fin_de_anio = 365 - ((sum(dias_por_mes[:mes])) + dia)

    return dias_faltantes_fin_de_anio

def dias_transcurridos_hasta_la_fecha(dia, mes, anio):

    if es_bisiesto(anio) == True:
        dias_por_mes[3] = 29
        dias_transcurridos = sum(dias_por_mes[:mes]) + dia
    else:
        dias_transcurridos = sum(dias_por_mes[:mes]) + dia

    return dias_transcurridos

def calcular_tiempo_transcurrido(dia1, mes1, anio1, dia2, mes2, anio2):

    if es_bisiesto(anio1) == True and es_bisiesto(anio2) == True:
        dias_por_mes[3] = 29
        tiempo1 = dia1 + sum(dias_por_mes[:mes1]) + anio1 * 366
        tiempo2 = dia2 + sum(dias_por_mes[:mes2]) + anio2 * 366

    elif es_bisiesto(anio1) == True:
        dias_por_mes[3] = 29
        tiempo1 = dia1 + sum(dias_por_mes[:mes1]) + anio1 * 366
        dias_por_mes[3] = 28
        tiempo2 = dia2 + sum(dias_por_mes[:mes2]) + anio2 * 365
    elif es_bisiesto(anio2) == True:
        tiempo1 = dia1 + sum(dias_por_mes[:mes1]) + anio1 * 365
        dias_por_mes[3] = 29
        tiempo2 = dia2 + sum(dias_por_mes[:mes2]) + anio2 * 366
    else:
        tiempo1 = dia1 + sum(dias_por_mes[:mes1]) + anio1 * 365
        tiempo2 = dia2 + sum(dias_por_mes[:mes2]) + anio2 * 365

    diferencia_dias = tiempo2 - tiempo1
    diferencia_meses = tiempo2 // 30 - tiempo1 // 30
    diferencia_anios = tiempo2 // 365 - tiempo1 // 365

    return diferencia_dias, diferencia_meses, diferencia_anios

calcular_tiempo_transcurrido(23,7,2002,23,8,2004)