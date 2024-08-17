# Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identificador, descripción, precio), y una lista de los productos a facturar, en la que cada uno consiste en una tupla de (identificador, cantidad). Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el precio total de cada producto comprado, y al final imprima el total general. Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.

def imprimir_factura(productos, prod_facturar) -> None:
    
    id, descripción, precio = productos
    precio_total = 0
    total_compra = 0

    print('Factura:')
    print('-'*10)
    for id_factura, cantidad in prod_facturar:
        for id, descripción, precio in productos:
            if id_factura == id :   
                precio_total += precio * cantidad
                print('\n' + f"ID: {id_factura}" + '\n' + f'cantidad: {cantidad}' + '\n' + f'Descripcion: {descripción}' + '\n' + f'Precio unitario: ${precio}' + '\n' + f'Precio total: ${precio_total}')
                total_compra += precio_total
                precio_total = 0
    print('-'*10)
    print(f'TOTAL COMPRA: ${total_compra}')

imprimir_factura([('1','Leche', 1000),('2','Coca', 1200), ('3', 'Pollo', 3000)], [('2',5), ('3',2)])

