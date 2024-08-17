# Programa para calcular el costo de uso de un teléfono.

def main():
    """El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo."""

    p = float(input("¿Cuánto cuesta 1 segundo de comunicacion?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))
    for x in range(n):
        h = int(input("¿Cuántas horas?: "))
        m = int(input("¿Cuántos minutos?: "))
        s = int(input("¿Cuántos segundos?: "))
        duracion = a_segundos(h, m, s)
        costo = duracion * p
        print("Duracion:", duracion, "segundos. Costo: $", costo)

def a_segundos(horas, minutos, segundos):
    """Transforma en segundos una medida de tiempo expresada en
        20 horas, minutos y segundos"""

    return 3600 * horas + 60 * minutos + segundos

main()