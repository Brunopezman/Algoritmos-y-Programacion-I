# Escribir una función empaquetar para una lista, donde empaquetar significa indicar la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1) , (1, 2), (3, 2)]

def empaquetar(lista:list):

    valor_actual = lista[0]
    cantidad = 1
    lista_valor_cantidad = []
    
    for i in range (1,len(lista)):

        if lista[i] == valor_actual:
            cantidad +=1
        else:
            lista_valor_cantidad.append((valor_actual, cantidad))
            valor_actual = lista[i]
            cantidad = 1

    lista_valor_cantidad.append((valor_actual, cantidad))

    return lista_valor_cantidad

print(empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]))