"""
Implementar el método __str__ de ListaEnlazada, para que se genere una
salida legible de lo que contiene la lista, similar a las listas de python
"""
class _Nodo:

    def __init__(self, dato, prox) -> None:
        self.dato = dato 
        self.prox = None 
    
class ListaEnlazada:

    def __init__(self) -> None:
        self.prim = None 
        self.len = 0

    def append(self, dato):
        
        #Cubrimos la excepcion de la lista vacia
        if not self.prim:
            self.prim = _Nodo(dato, None)
        else:
            #Si estaba inicializada con un dato ponemos al primer lugar como el actual.
            act = self.prim

            while act.prox:
                act = act.prox

            # act.proximo == None
            # act es el ultimo nodo de la lista. Le agregamos un dato.
            act.prox = _Nodo(dato, None)
        self.len += 1

    def __str__(self) -> str:
        
        # Imprimimos si es que esta vacia
        if not self.prim:
            return 'Lista vacía'

        elementos = []
        act = self.prim

        # Cuando pase que self.prim sea None, devolvera la lista en el formato deseado.
        while act:
            elementos.append(str(act.dato))
            act = act.prox

        return '[' + ', '.join(elementos) + ']'
    
    def pop_last(self, i):

        if not self.prim:
            return
        if i >= self.len:
            raise IndexError
        
        act = self.prim
        contador = 1 

        while act.prox:
            if contador == (self.len - i - 1):
                e = act.prox.dato
                act.prox = act.prox.prox
                return e
            
            contador += 1
            act = act.prox
    
# Ejemplo de uso:
l = ListaEnlazada()
l.append(3)
l.append(4)
l.append(7)
l.append(9)
l.append(5)
l.append(6)
numero = l.pop_last(2)
print(l)