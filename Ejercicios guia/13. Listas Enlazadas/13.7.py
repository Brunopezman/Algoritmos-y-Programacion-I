"""
Una lista circular es una lista cuyo último nodo está ligado al primero, de modo
que es posible recorrerla infinitamente. Escribir la clase ListaCircular, incluyendo los métodos insert, append, remove y pop
"""

class _Nodo:

    def __init__(self, dato) -> None:
        self.dato = dato
        self.prox = None

class ListaEnlazada:

    def __init__(self) -> None:
        self.prim = None
        self.len = 0

    def __str__(self) -> str:
        
        if not self.prim:
            return 'Lista vacía'

        elementos = []
        act = self.prim

        while act:
            elementos.append(str(act.dato))
            act = act.prox

        return '[' + ', '.join(elementos) + ']'

    def append(self, dato):
        
        if self.prim is None:
            self.prim = _Nodo(dato)
        else:

            act = self.prim

            while act.prox:
                act = act.prox
            act.prox = _Nodo(dato)
            
        self.len += 1

    def pop(self, i):
        pass

    def remove(self,x):
        pass

    def insert(self,dato,x):
        pass    

l = ListaEnlazada()
l.append(1)
l.append(2)
l.append(3)
# l.pop(2)
print(l)