# Escribir dos funciones que permitan calcular:
# a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
# b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

def a_segundos(h,m,s):
    
    return h*3600 + m*60 + s

def a_hms(segundos_totales):
    h = segundos_totales // 3600
    m = (segundos_totales % 3600) // 60
    s = segundos_totales
    
    return h, m, s

# Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

def main():

    print("Escriba dos intervalos de tiempo en horas, minutos y segundos para que luego sean sumados.")

    segundos_totales = 0

    for i in range(2):
        h = int(input("Cantidad de horas: "))
        m = int(input("Cantidad de minutos: "))
        s = int(input("Cantidad de segundos: "))

        segundos_totales += a_segundos(h,m,s)

    h, m, s = a_hms(segundos_totales)

    print("la duración total es de "+ str(h) +" hora/s, " + str(m) + " minuto/s y "+ str(s)+ " segundo/s ")

# main()

