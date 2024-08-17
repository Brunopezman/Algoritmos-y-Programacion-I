# Dada una lista, escribir una funcion que elimine los elementos en las posiciones pares.

def eliminar_e_en_pos_par(lista):

    for i in range(len(lista)-1,-1,-1):
        if i % 2 == 0:
           lista.pop(i)
    
    return lista

#Otra solucion

def eliminar_e_en_pos_par_2(lista):
    i = 0
    while i < len(lista):
        lista.pop(i)
        i += 1
        
    return lista

# Dadas dos matrices, devolver la suma de ambas

def sumar_matrices(m1:list[list], m2:list[list]):

    """Le suma a la matriz m1 la matriz m2, y la retorna como lista de filas"""

    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return "Las matrices deben tener las mismas dimensiones para sumarse." 
         
    for f in range(len(m1)):
        for c in range(len(m1[f])):
           m1[f][c] += m2[f][c]
    
    return m1

# Un crucigrama es una matriz de nxm que contiene celdas. Las celdas son tuplas de dos elementos de la forma (<color>, <contenido>). Cada celda puede ser BLANCA o NEGRA. El contenido es una cadena, si está vacía, la celda está vacía. Un crucigrama no está correctamente llenado si:
# Hay una celda BLANCA vacía
# Hay una celda NEGRA llena
# Escribir una función que dado un crucigrama, devuelva si está correctamente llenado

def verificar_crucigrama(crucigrama):
    for fila in crucigrama:
        for color, contenido in fila:
            if color == 'blanca' and not contenido or color == 'negra' and contenido:
                return False
    return True
            
# primer parcialito del primer cuatrimestre de 2013
# - Escribir una funcion que reciba por parametro una lista de numeros y devuelva otra lista con los numeros de la ingresada que terminan en cero. Por ejemplo, si se recibe la lista: [4, 23, 40, -7, 0, 14, 1000, -760] debe devolver [40, 0, 1000, -760].

def listar_n_con_cero_al_final(lista_numeros:list) -> list:
    terminados_en_cero = []
    for numero in lista_numeros:
        n = str(numero)
        if '0' in n[-1]:
            n = int(n)
            terminados_en_cero.append(n)
    
    return terminados_en_cero

# Escribir una funcion que pida cadenas al usuario hasta que ingrese una cadena vacıa. Debe devolver una lista de las palabras ingresadas.

def listar_palabras_ingresadas() -> list[str]:
  
    frase = ''
    
    while True:
        s = input('Ingrese una cadena: ')
        if not s:
            break  
        frase += s
    return frase.split()

#  Escribir una funcion que dada una matriz representada como una lista de listas de numeros (donde cada sublista representa una fila), devuelva una lista con los maximos de cada columna.

def maximos_columnas(matriz):
    maximos = []

    if not matriz:
        return maximos
    
    for c in range(len(matriz[0])):
        maximo = matriz[0][c] #IMPORTANTE guardarse el primer elemento
        for f in range(len(matriz)): #Iterando por columnas
            if matriz[f][c] > maximo:
                maximo = matriz[f][c]
        maximos.append(maximo)
    return maximos

"""Escribir una funcion que reciba una palabra y devuelva una lista con todas las rotaciones
de esa palabra. Por ejemplo, si recibe: 'rotar', debe devolver:
['rotar','otarr','tarro','arrot','rrota']"""

def obtener_rotaciones(palabra):
    rotaciones = []
    for i in range(len(palabra)):
        rotaciones.append(palabra[i:] + palabra[:i])
    return rotaciones

# Escribir una funcion que reciba dos secuencias y devuelva una lista con los elementos comunes a ambas, sin repetir ninguno.

def listar_e_comun(secuencia1:list, secuencia2:list) -> list:
    comunes = []
    for e in secuencia1:
        if e in secuencia2 and e not in comunes:
            comunes.append(e)

    return comunes

# Escribir una funcion que imprima los numeros de 1 a 100; pero para los multiplos de 3 imprima “Miki” en lugar del numero; y para los multiplos de 5 imprima “Moko”. Para los multiplos de 3 y 5 debe imprimir “MikiMoko”.

def mikimoko():
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            print('Mikimoko')
        elif n % 3 == 0:
            print('Miki')
        elif n % 5 == 0:
            print('Moko')
        else:
            print(n)

# Se pide implementar una función que reciba por parámetro una contraseña (en forma de cadena) y verifique que la misma sea válida, devolviendo un valor booleano. Para que una contraseña sea válida, debe cumplir con los siguientes requisitos:
# Debe tener entre 10 y 20 caracteres
# Si tiene menos de 15 caracteres, debe contener al menos dos vocales maýusculas
# Si tiene al menos 15 caracteres, no debe contener ninguno de los siguientes símbolos: % $ - ( ) = # ! ?

def verificar_contrasenia(contrasenia):

    if not 10 < len(contrasenia) < 20:
        return False
    
    if len(contrasenia) < 15:
        n_vocal_mayus = 0
        for c in contrasenia:
            if c.isupper() and c in "AEIOU":
                n_vocal_mayus += 1
        if not n_vocal_mayus >= 2:
            return False
    
    if len(contrasenia) >= 15 and '%$-()=#!?' in contrasenia:
        return False
    
    return True

# Escribir una función que reciba dos cadenas, texto y palabra, y devuelva una cadena igual a texto pero con todas las ocurrencias de palabra censuradas (es decir, reemplazados sus caracteres por *).

def devolver_t_censurado(t,p):  
    return t.replace(p,'*')

# Dada una matriz de enteros representada como una lista de listas donde cada sublista representa una fila de la matriz, escribir una función que devuelva una lista con la suma de los elementos de cada columna.

def sumar_e_columna(matriz):
    lista_suma = []
    suma_columna = 0
    for c in range(len(matriz[0])):
        for f in range(len(matriz)):
            suma_columna += matriz[f][c]
        lista_suma.append(suma_columna)
        suma_columna = 0
    
    return lista_suma

# Programa que pida lineas de texto. 

def enmarcar_texto():
    
    marco = 15*'*'
    while True:
        palabra = input('texto: ')
        if palabra >= 15:
            palabra = input('Ingrese un texto mas corto: ')
        espacio = (11 - len(palabra))* ' '
        if not palabra:
            marco += '\n' + 15*'*'
            print(marco)
            break
        
        marco += '\n' + '* ' + palabra + espacio  + ' *'

# for x in range(2, 29, 7):
#     print("Valor al inicio de la iteracion:", x)
#     x = (x * 2) - 3
#     print("Valor al final de la iteracion:", x)
# a. Hacer una tabla con los valores de x iniciales y finales de cada iteración. En caso de que el ciclo no termine nunca, colocar una fila con "...".
# b. Transformar el ciclo anterior a un ciclo while que implemente el mismo comportamiento.

# x = 2
# while x < 29:
#     print("Valor al inicio de la iteracion:", x)
#     x2 = (x * 2) - 3
#     print("Valor al final de la iteracion:", x2)
#     x += 7

# Escribir una función que reciba una cadena y devuelva el resultado de reemplazar todas las apariciones de la primera letra (ignorando mayúsculas o minúsculas) con un asterisco.

def primera_letra_con_asterisco(s):
    
    frase = ''
    for caracter in range(len(s)):
        if s[caracter] == s[0]:
            frase += '*'
        else:
            frase += s[caracter]
    
    return frase

