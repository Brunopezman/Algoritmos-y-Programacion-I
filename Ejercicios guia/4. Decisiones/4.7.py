# Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños y el programa le debe decir a qué signo corresponde.

def astrologia(dia,mes):

    if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
        return 'Aries'
    elif (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
        return 'Tauro'
    elif (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
        return 'Geminis'
    elif (dia >= 22 and mes == 6) or( dia <= 23 and mes == 7):
        return 'Cancer'
    elif dia >= 24 and mes == 7 or dia <= 23 and mes == 8:
        return 'Leo'
    elif (dia >= 24 and mes == 8) or (dia <= 23 and mes == 9):
        return 'Virgo'
    elif (dia >= 24 and mes == 9) or (dia <= 22 and mes == 10):
        return 'Libra'
    elif (dia >= 23 and mes == 10) or (dia <= 22 and mes == 11):
        return 'Escorpio'
    elif (dia >= 23 and mes == 11) or (dia <= 21 and mes == 12):
        return 'Sagitario'
    elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
        return 'Capricornio'
    elif (dia >= 21 and mes == 1) or (dia <= 19 and mes == 2):
        return 'Acuario'
    else:
        return 'Piscis'
    
def main():
    dia = int(input("Ingrese el dia de su cumpleanios: "))
    mes = int(input("Ingrese el dia de su cumpleanios: "))

    print(astrologia(dia,mes))

main()

